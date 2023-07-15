
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
        for plt in self._plates:
            print(f"| (ID: {plt.plate_id}) - {plt.name} (${plt.price})")
        print("-------------------------------------\n")

    # TODO: Add admin validation
    def add_new_plate(self, dish_name: string, price: float):
        new_id = len(self._plates) + 1
        self._plates.append(Plate(new_id, dish_name, price))

    # TODO: Add admin validation
    def remove_plate(self, plate_id: int):
        if plate_id < 1 or plate_id > len(self._plates):
            print("Invalid ID.")
            return

        # Check correctness (Process may be simple with a DB)
        plate_to_delete: Plate
        for plt in self._plates:
            if plt.plate_id == plate_id:
                plate_to_delete = plt
            elif plt.plate_id > plate_id:
                plt.plate_id = plt.plate_id - 1

        self._plates.remove(plate_to_delete)
        print("Plate removed successfully.")

    def does_plate_exist(self, plate_id: int):
        for plt in self._plates:
            if plt.plate_id == plate_id:
                return True
        print("Plate was not found.")
        return False

    def find_plate(self, plate_id: int):
        for plt in self._plates:
            if plt.plate_id == plate_id:
                return plt
        print("Error(find_plate).")


# plate = PlateService()
# plate.display_menu()
#
# plate.remove_plate(3)
# plate.remove_plate(4)
# plate.add_new_plate("caca", 12.8)
# plate.display_menu()

