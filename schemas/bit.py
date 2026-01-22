from pydantic import BaseModel, Field, ConfigDict

class Bit(BaseModel):
    diameter: float = Field(...,description="Diameter of the casing")
    type: str = Field(...,description="Type of the casing")

    model_config = ConfigDict(from_attributes=True)
    