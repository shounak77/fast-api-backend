from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, get_db, DbBase
import schemas.tariff as tariff_schema
# from schemas.tariff import TariffCreate
import crud.tariff as crud


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


DbBase.metadata.create_all(bind=engine) 

app = FastAPI()

@app.post("/tariffs/", response_model=tariff_schema.Tariff)
def create_tariff(tariff: tariff_schema.TariffCreate, db: Session = Depends(get_db)):
    """Create tariff."""
    return crud.create_tariff(db=db, tariff=tariff)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)