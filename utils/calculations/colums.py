from schemas.graph_pressure import HydraulicResult
from schemas.well_constraction import CasingDepth


def needs_casing(
    anomaly_current: float,
    anomaly_next: float,
    frac_current: float,
    frac_next: float
    ) -> bool:
    return (frac_next <= anomaly_current
            or anomaly_next >= frac_current)


def define_column(intervals:list[HydraulicResult])-> list[CasingDepth]:
    shoe_depths = []
    for i in range(len(intervals)-1):
        current = intervals[i]
        next = intervals[i+1]

        anomaly_current = current.anomaly_coefficient
        anomaly_next = next.anomaly_coefficient
        frac_current = current.fracturing_coefficient
        frac_next = next.fracturing_coefficient
        if needs_casing(anomaly_current, anomaly_next, frac_current, frac_next):
            shoe_depths.append(next.depth_up_m)
    return [CasingDepth(column_depth=depth, column_name=f"column {i}")
            for i, depth in enumerate(shoe_depths, start=1)]