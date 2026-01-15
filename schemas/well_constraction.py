from pydantic import BaseModel, Field, ConfigDict
from enum import Enum
from typing import Optional

class FluidType(str, Enum):
    GAS = "gas"
    OIL = "oil"

class ConductorInputParams(BaseModel):
    fluid: FluidType
    fluid_density: float = Field(...,ge=0, description="Density of the fluid, kg/m^3")
    pressure: float = Field(...,ge=0, description="Reservoir Pressure, MPa")
    frac_press1: float = Field(...,ge=0, description="1 Fraction of pressure, MPa")
    frac_press2: float = Field(...,ge=0, description="2 Fraction of pressure, MPa")
    depth1: int = Field(...,ge=0, description="1 Fraction of depth, m")
    depth2: int = Field(...,ge=0, description="2 Fraction of depth, m")
    depth_form: int = Field(...,ge=0, description="Reservoir depth, m")
    Z: Optional[int] = Field(default=0, ge=0, description="Well depth, m")
    t1: Optional[int] = Field(default=0, ge=0, description="1 Well temperature, C")
    t2: Optional[int] = Field(default=0, ge=0, description="2 Well temperature, C")

class ColumnResponse(BaseModel):
    column_depth: float = Field(..., description="Depth of the conductor, cm")
    column_name: str = Field(...,description="Name of the column")

    model_config = ConfigDict(from_attributes=True)

class CasingDepth(BaseModel):
    column_depth: int
    column_name: str = Field(...,description="Name of the column")
    model_config = ConfigDict(from_attributes=True)