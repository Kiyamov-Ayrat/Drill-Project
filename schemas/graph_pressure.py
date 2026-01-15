from pydantic import (BaseModel, Field,
                      PositiveFloat, PositiveInt, ConfigDict)
from typing import Optional

class HydraulicInput(BaseModel):
    pressure_mpa: PositiveFloat = Field(..., description="Pressure input in MPa")
    fracturing_pressure_mpa: Optional[float] = Field(default=None, description="Fraturing pressure input in MPa")
    depth_up_m: int = Field(..., ge=0, description="Depth up input in m")
    depth_down_m: PositiveInt = Field(..., description="Depth down input in m")

class HydraulicResult(BaseModel):
    id: Optional[int] = None
    pressure_mpa: float
    depth_up_m: int
    depth_down_m: int
    anomaly_coefficient: float
    fracturing_pressure_mpa: float
    fracturing_coefficient: float
    fracturing_coefficient2: float
    mud_density: float

    model_config = ConfigDict(from_attributes=True)