from cart import CartService


class CustomerService:
    _cart_service: CartService

    def __init__(self, cart_service: CartService):
        self._cart_service = cart_service

    def run_customer(self):
        selection = ""
        while selection != "-o":
            total = self._cart_service.get_total()

            if total == 0:
                selection = input("-b(buy), -o(log out):")
            else:
                selection = input("-b(buy), -p(pay), -r(remove), -o(log out):")

            if selection == "-b":
                plate_id = int(input("Enter ID to add plate:"))
                quantity = int(input("Enter quantity:"))
                self._cart_service.add_plate(plate_id, quantity)
                self._cart_service.display_cart()
            elif selection == "-p" and total != 0:
                self._cart_service.pay_cart()
            elif selection == "-r" and total != 0:
                plate_id = int(input("Enter ID to add plate:"))
                self._cart_service.remove_plate(plate_id)
                self._cart_service.display_cart()

        print("You have successfully logged out.")
