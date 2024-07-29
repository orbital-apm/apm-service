from fastapi import HTTPException, status

from app.utils.cryptography import decode_jwt


def get_current_user_id(token: str) -> str:
    try:
        return decode_jwt(token)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid authentication credentials",
                            headers={"WWW-Authenticate": "Bearer"})
