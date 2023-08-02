from login import LoginService
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
            print(f"| [ID:{plt.plate_id}] - {plt.name} (${plt.price})")
        print("-------------------------------------\n")

    def create_plate(self, plate_name: string, price: float):
        if self.does_plate_exist_by_name(plate_name):
            print("Plate already exists.")
            return

        new_id = len(self._plates) + 1
        self._plates.append(Plate(new_id, plate_name, price))
        print("Plate created successfully.")

    def delete_plate(self, plate_id: int):
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

    def does_plate_exist_by_id(self, plate_id: int):
        for plt in self._plates:
            if plt.plate_id == plate_id:
                return True
        return False

    def does_plate_exist_by_name(self, plate_name: string):
        for plt in self._plates:
            if plt.name == plate_name:
                return True
        return False

    def find_plate(self, plate_id: int):
        for plt in self._plates:
            if plt.plate_id == plate_id:
                return plt
        print("Error(find_plate).")


