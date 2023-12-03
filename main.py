from pydantic import BaseModel
from typing import Optional, List, Dict


class User(BaseModel):
    name: str
    mail: str
    address: str


class Banks(User):
    name: str
    rating: Optional[str] = '0/10'
    condition: Optional[str] = 'closed'


class Cards(Banks):
    bank: list = [Banks.name, Banks.rating, Banks.condition]
    cardholder: str = Banks.name
    condition: str


class Balance(Cards):
    card: Cards
    amount: Optional[int] = 0
    currency: str
