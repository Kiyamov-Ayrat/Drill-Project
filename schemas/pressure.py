from pydantic import BaseModel, ConfigDict

class PressureCreate(BaseModel):
    density: int
    depth: int

class PressureUpdate(BaseModel):
    density: int | None = None
    depth: int | None = None
    # pressure: int | None = None

    model_config = ConfigDict(from_attributes=True)

class PressureResponse(PressureCreate):
    id: int
    pressure: int

    class Config:
        from_attributes = True