from pydantic import BaseModel


class Client(BaseModel):
    id: int
    username: str
    owner_id: int

    class Config:
        from_attributes = True
