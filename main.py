from fastapi import FastAPI

from database import engine, DbBase

from routers.v1.tariff_router import router as tariff_router_v1
from routers.v2.tariff_router import router as tariff_router_v2

app = FastAPI(
    title="Tariff API",
    description="API for CRUD operations of tariffs",
    version="2.0",
)

DbBase.metadata.create_all(bind=engine)

app.include_router(tariff_router_v1, prefix="/v1", tags=["Tariffs v1"])
app.include_router(tariff_router_v2, prefix="/v2", tags=["Tariffs v2"])


@app.get("/")
def root():
    return {"message": "Welcome to the Tariff API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)