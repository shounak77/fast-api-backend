from sqlalchemy.orm import Session

from models.tariff import TariffORM
import schemas.tariff as schema


def create_tariff(db: Session, tariff: schema.TariffCreate) ->TariffORM:
    db_tariff = TariffORM(**tariff.model_dump())
    db.add(db_tariff)
    db.commit()
    db.refresh(db_tariff)
    return db_tariff