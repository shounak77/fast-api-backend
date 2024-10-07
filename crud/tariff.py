from typing import Optional

from sqlalchemy.orm import Session
from models.tariff import TariffORM
import schemas.tariff as schema


def create_tariff(db: Session, tariff: schema.TariffCreate) ->TariffORM:
    db_tariff = TariffORM(**tariff.model_dump())
    db.add(db_tariff)
    db.commit()
    db.refresh(db_tariff)
    return db_tariff

def get_tariff_by_id(db: Session, tariff_id: int) -> Optional[TariffORM]:
    return db.query(TariffORM).filter(TariffORM.id == tariff_id).first()


def update_tariff(db: Session, tariff_id: int, updated_tariff: schema.TariffCreate) -> Optional[TariffORM]:
    db_tariff = db.query(TariffORM).filter(TariffORM.id == tariff_id).first()
    if db_tariff:
        for key, value in updated_tariff.model_dump().items():
            setattr(db_tariff, key, value)
        db.commit()
        db.refresh(db_tariff)
    return db_tariff

def delete_tariff(db: Session, tariff_id: int) -> Optional[TariffORM]:
    db_tariff = db.query(TariffORM).filter(TariffORM.id == tariff_id).first()
    if db_tariff:
        db.delete(db_tariff)
        db.commit()
    return db_tariff