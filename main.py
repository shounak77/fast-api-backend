from fastapi import FastAPI

from database import engine, DbBase

from routers.v1.tariff_router import router as tariff_router_v1
from routers.v2.tariff_router import router as tariff_router_v2

import logging
import graypy

logger = logging.getLogger("backend_logger")
logger.setLevel(logging.INFO)


graylog_handler = graypy.GELFUDPHandler(host='127.0.0.1', port=12201)
formatter = logging.Formatter(
    '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "module": "%(module)s", "message": "%(message)s"}'
)
graylog_handler.setFormatter(formatter)
logger.addHandler(graylog_handler)

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
    logger.info("Root endpoint called")
    return {"message": "Welcome to the Tariff API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)