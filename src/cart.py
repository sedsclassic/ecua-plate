from plate import PlateService


class CartService:
    _cart = {}  # int:Plate
    _plate_service: PlateService

    def __init__(self, service: PlateService):
        self._plate_service = service

    def add_plate(self, plate_id: int, quantity: int):
        if not self._plate_service.does_plate_exist_by_id(plate_id):
            print("Plate was not found.")
            return

        if plate_id not in self._cart:
            self._cart[plate_id] = quantity
        else:
            self._cart[plate_id] += quantity

    def remove_plate(self, plate_id: int):
        if plate_id in self._cart:
            del self._cart[plate_id]
        else:
            print("Invalid ID.\n")

    def display_cart(self):
        print("----------------CART-----------------")
        total = 0
        for plate_id in self._cart:
            plate = self._plate_service.find_plate(plate_id)
            print(f"| [ID:{plate_id}] - {plate.name}: Qty({self._cart[plate_id]}) (${plate.price * self._cart[plate_id]})")
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



