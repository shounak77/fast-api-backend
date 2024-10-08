import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas.tariff as tariff_schema
import crud.tariff as crud
from database import get_db

router = APIRouter()

logger = logging.getLogger("backend_logger")

@router.post("/tariffs/", response_model=tariff_schema.Tariff)
def create_tariff(tariff: tariff_schema.TariffCreate, db: Session = Depends(get_db)):
    """Create a new tariff"""
    logger.info("Creating a new tariff with details: %s", tariff)
    created_tariff = crud.create_tariff(db=db, tariff=tariff)
    logger.info("Tariff created with ID: %d", created_tariff.id)
    return created_tariff

@router.get("/tariffs/{tariff_id}", response_model=tariff_schema.Tariff)
def read_tariff(tariff_id: int, db: Session = Depends(get_db)):
    """Retrieve a tariff by ID"""
    logger.info("Retrieving tariff with ID: %d", tariff_id)
    db_tariff = crud.get_tariff_by_id(db=db, tariff_id=tariff_id)
    if db_tariff is None:
        logger.warning("Tariff with ID %d not found", tariff_id)
        raise HTTPException(status_code=404, detail="Tariff not found")
    logger.info("Tariff retrieved! ID: %d", db_tariff.id)
    return db_tariff

@router.put("/tariffs/{tariff_id}", response_model=tariff_schema.Tariff)
def update_tariff(tariff_id: int, tariff: tariff_schema.TariffCreate, db: Session = Depends(get_db)):
    logger.info("Updating tariff with ID: %d, new details: %s", tariff_id, tariff)
    db_tariff = crud.update_tariff(db=db, tariff_id=tariff_id, updated_tariff=tariff)
    if db_tariff is None:
        logger.warning("Tariff with ID %d not found for update", tariff_id)
        raise HTTPException(status_code=404, detail="Tariff not found")
    logger.info("Tariff updated successfully! ID: %d", db_tariff.id)
    return db_tariff

@router.delete("/tariffs/{tariff_id}", response_model=tariff_schema.Tariff)
def delete_tariff(tariff_id: int, db: Session = Depends(get_db)):
    """Delete a tariff by ID"""
    logger.info("Deleting tariff with ID: %d", tariff_id)
    db_tariff = crud.delete_tariff(db=db, tariff_id=tariff_id)
    if db_tariff is None:
        logger.warning("Tariff with ID %d not found for deletion", tariff_id)
        raise HTTPException(status_code=404, detail="Tariff not found")
    logger.info("Tariff deleted successfully! ID: %d", db_tariff.id)
    return db_tariff
