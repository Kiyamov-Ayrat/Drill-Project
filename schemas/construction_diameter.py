from pydantic import BaseModel, ConfigDict


class Diameter(BaseModel):
    column_depth: float
    column_name: str
    column_diameter: float
    bit_diameter: float

    model_config = ConfigDict(from_attributes=True)