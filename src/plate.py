
from dataclasses import dataclass
import string


@dataclass
class Plate:
    name: string
    price: float


class PlateService:
    plates = {
        # id: plate
        1: Plate("Chugchucara", 9.99),
        2: Plate("Churrasco", 4.99),
        3: Plate("Llapingacho", 7.99),
        }

    def display_menu(self):
        for key in self.plates:
            print(f"{self.plates[key].name} (${self.plates[key].price}): {key}")

    def add_plate(self, dish_name: string, price: int):
        self.plates[len(self.plates)+1] = Plate(dish_name, price)

#add_plate("Encebollado", 2.99)
#display_menu()

# while(True):
#     print("\nEnter code to add cart: ")
#     selection = int(input())
#
#     print(f"You have selected {PLATES[selection].name} (${PLATES[selection].price})")

