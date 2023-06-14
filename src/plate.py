
from dataclasses import dataclass
import string


@dataclass
class Plate:
    id: int
    name: string
    price: float
    image: string


PLATES = [
    Plate(111, "Chugchucara", 9.99, "zip"),
    Plate(222, "Churrasco", 4.99, "zip"),
    Plate(333, "Llapingacho", 7.99, "zip"),
    ]

selection = 

for i in PLATES:
    print(f"{i.name} - {i.price}")

