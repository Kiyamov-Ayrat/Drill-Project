from fastapi import FastAPI
from contextlib import asynccontextmanager
# from database.data import create_db_and_tables
from routers import pressure, graph_pressure, well, well_constraction, construction_diameter
from routers import debit_standard

@asynccontextmanager
async def lifespan(app: FastAPI):
    # create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"Hello": "World"}

# app.include_router(pressure.router)
app.include_router(graph_pressure.router)
app.include_router(well.router)

app.include_router(well_constraction.router)

app.include_router(construction_diameter.router)

app.include_router(debit_standard.router)