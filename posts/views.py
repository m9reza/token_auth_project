from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone  # Add this import
from .models import User, Post, RefreshToken
from .token_manager import generate_access_token, generate_refresh_token, validate_access_token, invalidate_refresh_token, REFRESH_TOKEN_EXPIRY
from datetime import timedelta
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            if not User.objects.filter(username=username).exists():
                User.objects.create(username=username, password=hash_password(password))
                return redirect("login")
            return HttpResponse("Username already exists")
        except Exception as e:
            return HttpResponse(f"Error during registration: {str(e)}")
    return render(request, "login.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username, password=hash_password(password))
            # Generate tokens
            access_token = generate_access_token(user.id)
            refresh_token = generate_refresh_token()
            RefreshToken.objects.create(
                user=user,
                token=refresh_token,
                expires_at=timezone.now() + timedelta(seconds=REFRESH_TOKEN_EXPIRY)  # Use timezone.now()
            )
            request.session["access_token"] = access_token
            request.session["refresh_token"] = refresh_token
            return redirect("home")
        except User.DoesNotExist:
            return HttpResponse("Invalid credentials")
        except Exception as e:
            return HttpResponse(f"Error during login: {str(e)}")
    return render(request, "login.html")



def logout(request):
    refresh_token = request.session.get("refresh_token")
    if refresh_token:
        invalidate_refresh_token(refresh_token)
    request.session.flush()
    return redirect("login")


def home(request):
    access_token = request.session.get("access_token")
    user_id = validate_access_token(access_token) if access_token else None
    if not user_id:
        return redirect("login")

    if request.method == "POST":
        content = request.POST["content"]
        Post.objects.create(user_id=user_id, content=content)
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "home.html", {"posts": posts})