import hashlib
import base64
import time
import secrets
import uuid  # Add this import
from datetime import datetime, timedelta

# Token settings
ACCESS_TOKEN_EXPIRY = 300  # 5 minutes in seconds
REFRESH_TOKEN_EXPIRY = 7 * 24 * 3600  # 7 days in seconds

def generate_access_token(user_id):
    # Simple token: user_id + timestamp + random secret
    timestamp = str(int(time.time()))
    random_secret = secrets.token_hex(16)
    token_string = f"{user_id}:{timestamp}:{random_secret}"
    # Encode to base64 for compactness
    token = base64.urlsafe_b64encode(token_string.encode()).decode()
    return token

def generate_refresh_token():
    # Use UUID from the database (stored in RefreshToken model)
    return str(uuid.uuid4())

def validate_access_token(token):
    try:
        decoded = base64.urlsafe_b64decode(token).decode()
        user_id, timestamp, _ = decoded.split(":")
        timestamp = int(timestamp)
        current_time = int(time.time())
        if current_time - timestamp > ACCESS_TOKEN_EXPIRY:
            return None  # Expired
        return int(user_id)  # Valid, return user_id
    except Exception:
        return None  # Invalid token

def invalidate_refresh_token(token):
    from .models import RefreshToken
    try:
        RefreshToken.objects.get(token=token).delete()
        return True
    except RefreshToken.DoesNotExist:
        return False