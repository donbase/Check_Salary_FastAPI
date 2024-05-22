import uuid
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    salary:int
    grow_salary_date:str = 'not planned'


class UserCreate(schemas.BaseUserCreate):
    salary: int
    grow_salary_date:str = 'not planned'

