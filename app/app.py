from fastapi import Depends, FastAPI
from app.db import User
from app.schemas import UserCreate, UserRead
from app.users import auth_backend, current_active_user, fastapi_users

app = FastAPI(title="Check Salary")

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["authentification"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["authentification"],
)

@app.get("/protected-route", tags=["Check salary"])
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"login": user.email, "salary": user.salary, "increase salary date":user.grow_salary_date}


# @app.on_event("startup")
# async def on_startup():
#     # Not needed if you setup a migration system like Alembic
#     await create_db_and_tables()



