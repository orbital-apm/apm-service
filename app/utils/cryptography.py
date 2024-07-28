import os
import time

import bcrypt
import jwt


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())


def generate_jwt(user_id: str) -> str:
    time_now = int(time.time())
    claims = {
        "sub": user_id,
        "iss": "apm-service",
        "iat": time_now,
        "exp": time_now + (int(os.getenv("ACCESS_TOKEN_VALIDITY_MINUTES", 15)) * 60)
    }

    # Todo: Consolidate env vars. Ensure not None.
    token = jwt.encode(payload=claims, key=os.getenv("ACCESS_TOKEN_SECRET_KEY"), algorithm="HS256")

    return token


def decode_jwt(token: str) -> str:
    try:
        decoded_token = jwt.decode(
            jwt=token,
            key=os.getenv("ACCESS_TOKEN_SECRET_KEY"),
            algorithms=["HS256"],
            options={"verify_exp": True}
        )
        return decoded_token.get("sub")
    
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
