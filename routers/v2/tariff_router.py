from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas.tariff as tariff_schema
import crud.tariff as crud
from database import get_db

from utils import success_response, error_response

router = APIRouter()

@router.post("/tariffs/")
def create_tariff_v2(tariff: tariff_schema.TariffCreate, db: Session = Depends(get_db)):
    """Create a new tariff"""
    try:
        new_tariff = crud.create_tariff(db=db, tariff=tariff)
        return success_response(new_tariff, "Tariff created successfully")
    except Exception as e:
        return error_response(500, "Failed to create tariff", [str(e)])