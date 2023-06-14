
from dataclasses import dataclass
import string


@dataclass
class Plate:
    name: string
    price: float


PLATES = {
    # id: plate
    1: Plate("Chugchucara", 9.99),
    2: Plate("Churrasco", 4.99),
    3: Plate("Llapingacho", 7.99),
    }

for key in PLATES:
    print(f"{PLATES[key].name} (${PLATES[key].price}): {key}")

while(True):
    print("\n\nEnter code to add cart: ")
    selection = int(input());

    print(f"You have selected {PLATES[selection].name} (${PLATES[selection].price})")

