from pydantic import BaseModel, ConfigDict

class WellCreate(BaseModel):
    name: str
    model_config = ConfigDict(from_attributes=True)

class WellResponse(WellCreate):
    id: int
