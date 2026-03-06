from pydantic import BaseModel

class Contract(BaseModel):
    id = int
    project_id = int
    terms: str
    signed: bool
    
    class Config:
        from_attributes = True