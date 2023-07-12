from dataclasses import dataclass
from plate import Plate, PlateService
import string


class CartService:
    _cart = {}
    _plate_service: PlateService

    def __init__(self, service: PlateService):
        self._plate_service = service

    def add_plate(self, plate_id: int, quantity: int):
        if not self._plate_service.does_plate_exist(plate_id):
            return

        if plate_id not in self._cart:
            self._cart[plate_id] = quantity
        else:
            self._cart[plate_id] += quantity

    def remove_plate(self):
        ...

    def display_cart(self):
        print("----------------CART-----------------")
        total = 0
        for plate_id in self._cart:
            plate = self._plate_service.find_plate(plate_id)
            print(f"| {plate.name}: Qty({self._cart[plate_id]}) (${plate.price * self._cart[plate_id]})")
            total += plate.price * self._cart[plate_id]
        print(f"* Total: ${total}")
        print("-------------------------------------\n")

    def get_total(self) -> float:
        total = 0
        for plate_id in self._cart:
            plate = self._plate_service.find_plate(plate_id)
            total += plate.price * self._cart[plate_id]
        return total

    def pay_cart(self):
        self._cart = {}
        print("Thanks for your shopping with us!")

# c = CartService(PlateService())
# c.add_plate(1, 2)
# c.add_plate(1, 1)
# c.add_plate(2, 1)
# c.add_plate(3, 7)
# c.add_plate(12, 7)
#
# c.display_cart()


