from io import BytesIO
import asyncio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sqlalchemy import select
from models.graph_pressure import Info
from database.data import SessionDep
from utils.calculations.graph_pressure import HydraulicResult
from fastapi.responses import StreamingResponse
# data = [
#   {
#     "pressure_mpa": 7,
#     "depth_up_m": 700,
#     "depth_down_m": 930,
#     "anomaly_coefficient": 1.0197162129779282,
#     "fracturing_pressure_mpa": 12.339,
#     "fracturing_coefficient": 0.7675283323489782,
#     "mud_density": 1.1216878342757213
#   },
#   {
#     "pressure_mpa": 9.3,
#     "depth_up_m": 930,
#     "depth_down_m": 1100,
#     "anomaly_coefficient": 1.0197162129779282,
#     "fracturing_pressure_mpa": 15.268,
#     "fracturing_coefficient": 0.8621237073358848,
#     "mud_density": 1.1216878342757213
#   },
#   {
#     "pressure_mpa": 10,
#     "depth_up_m": 1100,
#     "depth_down_m": 1200,
#     "anomaly_coefficient": 0.9270147390708439,
#     "fracturing_pressure_mpa": 16.560000000000002,
#     "fracturing_coefficient": 0.8497635108149403,
#     "mud_density": 1.0197162129779282
#   }
# ]

async def read_data(session: SessionDep, well_id: int):
  stmt = select(Info).where(Info.well_id==well_id)
  result = await session.scalars(stmt)
  data = result.all()
  return [HydraulicResult.model_validate(d) for d in data]

async def build_graphic(session: SessionDep, well_id: int):
  data = await read_data(session=session, well_id=well_id)
  anomaly_coef = []
  fracturing_coef = []
  fracturing_coef2 = []
  mud_dens = []
  depths = []

  for interval in data:
      anomaly_coef.extend([interval.anomaly_coefficient] * 2)
      fracturing_coef.extend([interval.fracturing_coefficient] * 2)
      fracturing_coef2.extend([interval.fracturing_coefficient2] * 2)
      mud_dens.extend([interval.mud_density] * 2)
      depths.extend([interval.depth_up_m, interval.depth_down_m])

  def plot_in_thread():
      plt.figure(figsize=(8, 10))

      # Построение линий
      plt.plot(anomaly_coef, depths, 'r-o', linewidth=2, markersize=6,
               label="Anomaly Coefficient")
      plt.plot(fracturing_coef, depths, 'g-o', linewidth=2, markersize=6,
               label="Fracturing Coefficient")

      plt.plot(fracturing_coef2, depths, 'y-o', linewidth=2, markersize=6,
               label="Fracturing Coefficient 2")
      plt.plot(mud_dens, depths, 'b-o', linewidth=2, markersize=6,
               label="Mud Density")

      # Настройки графика
      plt.title("Geomechanical Parameters", fontsize=14, fontweight='bold', pad=20)
      plt.xlabel("Value", fontsize=12, fontweight='bold')
      plt.ylabel("Depth (m)", fontsize=12, fontweight='bold')

      # Оформление
      plt.gca().invert_yaxis()  # Глубина увеличивается вниз
      plt.gca().xaxis.tick_top()
      plt.gca().xaxis.set_label_position('top')
      plt.grid(True, alpha=0.3, linestyle='--')

      # Легенда под графиком
      plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                 ncol=3, frameon=True, fancybox=True)

      # Настройка отступов
      plt.tight_layout(rect=[0, 0.05, 1, 0.95])

      buf = BytesIO()
      plt.savefig(buf, format='png')
      buf.seek(0)
      plt.close()
      return buf
  buf = await asyncio.to_thread(plot_in_thread)
  return StreamingResponse(buf, media_type='image/png')








