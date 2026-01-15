from schemas.graph_pressure import HydraulicInput, HydraulicResult
DENSITY_WATER = 1000.0
GRAVITY = 9.80665

def calculate_coefficient(pressure_mpa: float, depth_m: int)->float:
    if depth_m<0 or pressure_mpa<=0:
        raise ValueError("Pressure and depth input must be positive")
    elif depth_m==0:
        return 1.0
    hydrostatic = DENSITY_WATER*GRAVITY*depth_m/1_000_000
    return pressure_mpa/hydrostatic

def calculate_fracturing_pressure(pressure_mpa: float, depth_down_m: int)->float:
    return 0.0083*depth_down_m + 0.66*pressure_mpa

def calculate_fracturing_coefficient2(c_f: float)->float:
    return c_f*0.95

def calculate_mud_density(c_a: float, depth_down_m: int) -> float:
    if depth_down_m <= 1200:
        return c_a*1.1
    else:
        return c_a*1.05

def calculate_parameter(data: HydraulicInput) -> HydraulicResult:
    c_a = calculate_coefficient(data.pressure_mpa, data.depth_up_m)

    if data.fracturing_pressure_mpa is None:
        frac_p = calculate_fracturing_pressure(data.pressure_mpa, data.depth_down_m)
    else:
        frac_p = data.fracturing_pressure_mpa

    c_f = calculate_coefficient(frac_p, data.depth_down_m)
    c_f2 = calculate_fracturing_coefficient2(c_f)
    p = calculate_mud_density(c_a, data.depth_down_m)
    return HydraulicResult(
        pressure_mpa=data.pressure_mpa,
        depth_up_m=data.depth_up_m,
        depth_down_m=data.depth_down_m,
        anomaly_coefficient=c_a,
        fracturing_pressure_mpa=frac_p,
        fracturing_coefficient=c_f,
        fracturing_coefficient2=c_f2,
        mud_density=p
    )


def calculate_parameters_all(inputs: list[HydraulicInput]) -> list[HydraulicResult]:
    return [calculate_parameter(input) for input in inputs]


# if __name__ == "__main__":
#     raw_data = [
#         {"pressure_mpa": 7, "depth_up_m": 700, "depth_down_m": 930},
#         {"pressure_mpa": 8, "depth_up_m": 930, "depth_down_m": 1100},
#         {"pressure_mpa": 10, "depth_up_m": 1100, "depth_down_m": 1500},
#     ]
#
#     inputs = [HydraulicInput(**item) for item in raw_data]
#     results = calculate_parameters_all(inputs)
#
#     print(len(results))          # 3
#     print(results)