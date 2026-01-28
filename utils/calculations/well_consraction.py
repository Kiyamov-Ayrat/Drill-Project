from math import exp
from schemas.well_constraction import (ConductorInputParams,
                                       ColumnResponse,
                                       FluidType)
from fastapi import HTTPException

GRAVITY = 9.80665 #m/s^2

def calculate_conductor_depth(params: ConductorInputParams)->ColumnResponse:
    if params.depth1 == params.depth2:
        raise HTTPException(status_code=400, detail="zero division, depth1 or depth2 must be different")
    grad_p = (params.frac_press2 - params.frac_press1) / (params.depth2 - params.depth1)
    if params.fluid == FluidType.GAS:
        avg_temp = ((params.t1+273)+(params.t2+273))/2
        S = (0.034*params.fluid_density*(params.depth_form-params.Z))/(0.6*avg_temp)
        H_c = params.pressure/(exp(S)*grad_p)
        return ColumnResponse(column_depth=H_c,
                              column_name="conductor",)
    elif params.fluid == FluidType.OIL:
        hydrostatic = params.fluid_density*GRAVITY*params.depth_form
        H_c = (params.pressure-hydrostatic)/(grad_p-params.depth_form*GRAVITY)
        return ColumnResponse(column_depth=H_c,
                              column_name="conductor",)
    else:
        raise ValueError(f"Conductor concentration {params.fluid} not implemented")



params_gas = ConductorInputParams(
        fluid=FluidType.GAS,
        fluid_density=0.605,
        pressure=30.5,
        frac_press1=43.67,
        frac_press2=46.3,
        depth1=3050,
        depth2=3155,
        depth_form=3050,
        t1=21,
        t2=99
    )
params_oil = ConductorInputParams(
        fluid=FluidType.OIL,
        fluid_density=700,
        pressure=30.5,
        frac_press1=43.67,
        frac_press2=46.3,
        depth1=3050,
        depth2=3155,
        depth_form=3050
    )