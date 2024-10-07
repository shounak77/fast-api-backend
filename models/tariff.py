from sqlalchemy import Column, Integer, String, Numeric
from database import DbBase

class TariffORM(DbBase):
    __tablename__ = "tariffs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    rate = Column(Numeric, nullable=False)
    tax_rate = Column(Numeric, nullable=False)
    currency = Column(String(3), nullable=False)
    code = Column(String(5), nullable=False)
