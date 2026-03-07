from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str
    email: str
    password: str
    role: str

    model_config = {'from_attributes': True}


class UserResponseSchema(BaseModel):
    id: int
    username: str
    email: str
    role: str

    model_config = {'from_attributes': True}
