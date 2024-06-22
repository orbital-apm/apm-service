c
from app.db.database import get_db
from app.schemas.auth import LoginUserSchema, RegisterUserSchema
from app.services.auth_service import login_user, register_user

router = APIRouter()


@router.post("/login")
def login(returning_user: LoginUserSchema, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        # Todo: Refresh token.
        access_token = login_user(returning_user, db)

        response_payload = {
            "access_token": access_token,
            "token_type": "bearer"
        }

        return JSONResponse(response_payload)

    except HTTPException:
        raise

    except Exception:
        # Todo: Handle exceptions.
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/register")
def register(new_user: RegisterUserSchema, db: Session = Depends(get_db)) -> JSONResponse:
    try:
        register_user(new_user, db)

        # Todo: Return token.
        return JSONResponse({})

    except HTTPException:
        raise

    except Exception:
        # Todo: Handle exceptions.
        raise HTTPException(status_code=500, detail="Internal Server Error")


# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)) -> User:
#     credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                                           detail="Could not validate credentials",
#                                           headers={"WWW-Authenticate": "Bearer"},)
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except InvalidTokenError:
#         raise credentials_exception
#     user = db.query(User).filter(User.username == token_data.username).first()  # type: ignore
#     if user is None:
#         raise credentials_exception
#     return user
#
#
# async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)],) -> User:
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user.")
#     return current_user
#
#
# @router.get("/users/me/")
# async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]) -> User:
#     return current_user
