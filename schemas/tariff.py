from pydantic import BaseModel, constr, condecimal
from typing import Optional

class TariffBase(BaseModel):
    name: constr(min_length=1, max_length=100)
    description: Optional[str] = None
    rate: float #condecimal(gt=0)
    currency: constr(min_length=3, max_length=3)
    tax_rate: condecimal(ge=0)
    code: constr(min_length=5, max_length=5)

class TariffCreate(TariffBase):
    pass

class Tariff(TariffBase):
    id: int

    class ConfigDict: # mapping with ORM
        from_attributes = True

