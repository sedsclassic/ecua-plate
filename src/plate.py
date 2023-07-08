
from dataclasses import dataclass
import string


@dataclass
class Plate:
    plate_id: int
    name: string
    price: float


class PlateService:
    _plates = [
        Plate(1, "Chugchucara", 9.99),
        Plate(2, "Churrasco", 4.99),
        Plate(3, "Llapingacho", 7.99),
    ]

    def display_menu(self):
        print("----------------MENU-----------------")
        for plate in self._plates:
            print(f"| (ID: {plate.plate_id}) - {plate.name} (${plate.price})")
        print("-------------------------------------\n")

    def add_new_plate(self, dish_name: string, price: int):
        new_id = len(self._plates) + 1
        self._plates.append(Plate(new_id, dish_name, price))

    def does_plate_exist(self, plate_id: int):
        for plate in self._plates:
            if plate.plate_id == plate_id:
                return True
        print("Plate was not found.")
        return False

    def find_plate(self, plate_id: int):
        for plate in self._plates:
            if plate.plate_id == plate_id:
                return plate
        print("Error(find_plate).")


# plate = PlateService()
# plate.add_plate("Encebollado", 2.99)
# plate.display_menu()

