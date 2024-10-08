from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas.tariff as tariff_schema
import crud.tariff as crud
from database import get_db

router = APIRouter()

@router.post("/tariffs/", response_model=tariff_schema.Tariff)
def create_tariff(tariff: tariff_schema.TariffCreate, db: Session = Depends(get_db)):
    """Create a new tariff"""
    return crud.create_tariff(db=db, tariff=tariff)

@router.get("/tariffs/{tariff_id}", response_model=tariff_schema.Tariff)
def read_tariff(tariff_id: int, db: Session = Depends(get_db)):
    """Retrieve a tariff by ID"""
    db_tariff = crud.get_tariff_by_id(db=db, tariff_id=tariff_id)
    if db_tariff is None:
        raise HTTPException(status_code=404, detail="Tariff not found")
    return db_tariff

@router.put("/tariffs/{tariff_id}", response_model=tariff_schema.Tariff)
def update_tariff(tariff_id: int, tariff: tariff_schema.TariffCreate, db: Session = Depends(get_db)):
    """Update tariff by ID"""
    db_tariff = crud.update_tariff(db=db, tariff_id=tariff_id, updated_tariff=tariff)
    if db_tariff is None:
        raise HTTPException(status_code=404, detail="Tariff not found")
    return db_tariff

@router.delete("/tariffs/{tariff_id}", response_model=tariff_schema.Tariff)
def delete_tariff(tariff_id: int, db: Session = Depends(get_db)):
    """Delete a tariff by ID"""
    db_tariff = crud.delete_tariff(db=db, tariff_id=tariff_id)
    if db_tariff is None:
        raise HTTPException(status_code=404, detail="Tariff not found")
    return db_tariff
