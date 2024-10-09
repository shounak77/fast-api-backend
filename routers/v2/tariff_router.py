import logging 

from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
import schemas.tariff as tariff_schema
import crud.tariff as crud
from database import get_db

from utils import success_response, error_response

router = APIRouter()

logger = logging.getLogger("backend_logger")

@router.post("/tariffs/")
def create_tariff_v2(tariff: tariff_schema.TariffCreate, db: Session = Depends(get_db)):
    """Create a new tariff"""
    try:
        logger.info("Creating a new tariff with details: %s", tariff)
        new_tariff = crud.create_tariff(db=db, tariff=tariff)
        logger.info("Tariff created with ID: %d", new_tariff.id)
        return success_response(new_tariff, "Tariff created successfully")
    except OperationalError as e:
        logger.error("Failed to create tariff: %s", e)

        return error_response(400, "Failed to create tariff", [str(e)])
    
@router.get("/tariffs/{tariff_id}")
def read_tariff_v2(tariff_id: int, db: Session = Depends(get_db)):
    """Retrieve a tariff by ID"""
    logger.info("Retrieving tariff with ID: %d", tariff_id)
    db_tariff = crud.get_tariff_by_id(db=db, tariff_id=tariff_id)
    if db_tariff is None:
        logger.warning("Tariff with ID %d not found", tariff_id)
        return error_response(404, "Tariff not found", {"tariff_id": tariff_id})
    logger.info("Tariff retrieved! ID: %d", db_tariff.id)
    return success_response(db_tariff, "Tariff retrieved successfully")


@router.get("/tariffs/")
def read_tariffs(
    db: Session = Depends(get_db),
    name: Optional[str] = Query(None, description="Filter tariffs by name"),
    currency: Optional[str] = Query(None, description="Filter tariffs by currency"),
    rate: Optional[float] = Query(None, description="Filter tariffs by rate"),
    code: Optional[str] = Query(None, description="Filter tariffs by code"),
    tax_rate: Optional[float] = Query(None, description="Filter tariffs by tax rate"),
):
    """Fetch tariffs based on matched field"""

    try:
        logger.info("Querying tariffs with filters: name=%s, currency=%s, rate=%s, code=%s, tax_rate=%s", name, currency, rate, code, tax_rate)
        tariffs = crud.query_tariffs(
            db=db,
            name=name,
            currency=currency,
            rate=rate,
            code=code,
            tax_rate=tax_rate
        )
        return success_response(tariffs, "Tariffs retrieved successfully")
    
    except OperationalError as e:
        logger.error("Failed to create retrieve: %s", e)
        return error_response(400, "Unable to retrieve tariffs", [str(e)])
    
    
@router.put("/tariffs/{tariff_id}")
def update_tariff_v2(tariff_id: int, tariff: tariff_schema.TariffCreate, db: Session = Depends(get_db)):
    """Update tariff by ID (v2) with standard response."""
    try:
        logger.info("Updating tariff with ID: %s", tariff_id)
        db_tariff = crud.update_tariff(db=db, tariff_id=tariff_id, updated_tariff=tariff)
        if db_tariff is None:
            logger.warning("Tariff not found: %s", tariff_id)
            return error_response(404, "Tariff not found", {"tariff_id": tariff_id})
        logger.info("Tariff updated successfully: %s", db_tariff.id)
        return success_response(db_tariff, "Tariff updated successfully")
    except OperationalError as e:
        logger.error("Unable update tariff: %s", str(e))
        return error_response(500, "Failed to update tariff", [str(e)])
    

@router.delete("/tariffs/{tariff_id}")
def delete_tariff_v2(tariff_id: int, db: Session = Depends(get_db)):
    """Delete a tariff by ID (v2) with standard response."""
    try:
        logger.info("Deleting tariff with ID: %s", tariff_id)
        db_tariff = crud.delete_tariff(db=db, tariff_id=tariff_id)
        if db_tariff is None:
            logger.warning("Tariff not found: %s", tariff_id)
            return error_response(404, "Tariff not found", {"tariff_id": tariff_id})
        logger.info("Tariff deleted successfully: %s", db_tariff.id)
        return success_response(db_tariff, "Tariff deleted successfully")
    except OperationalError as e:
        logger.error("Uable to delete tariff: %s", str(e))
        return error_response(500, "Failed to delete tariff", [str(e)])