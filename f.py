import logging


# явная типизация

# def slojenie(a: int, b: int) -> dict:
#     return a + b
#
#
# def ymnoj(a: int, b: int) -> dict:
#     return a * b
#
#
# def minus(a: int, b: int) -> dict:
#     return a - b
#
#
# print(slojenie(1,2))
# print(ymnoj(1,2))
# print(minus(1,2))


#logging
from typing import Optional, List, Dict
from pydantic import BaseModel
import logging
#
#
# class User(BaseModel):
#     name: str
#     number: Optional[int]
#
#
# player1 = User(name="Pasha", number="qwe")
# print(player1.name)
# print(player1.number)
#
import logging

# Настройка логгера
# logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
#
#
#
# try:
#     a = a
# except Exception:
#     logging.warning('XA')



