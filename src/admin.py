from plate import Plate, PlateService
from login import LoginService, AccountType


class AdminService:
    _plate_service: PlateService
    _login_service: LoginService

    def __init__(self, login_service, plate_service):
        self._login_service = login_service
        self._plate_service = plate_service

    def run_admin(self):
        selection = ""
        while selection != "-o":
            selection = input("-mp(manage plates), -ma(manage accounts), -o(log out):")
            if selection == "-mp":

                while selection != "-c":
                    selection = input("-a(add plate), -r(remove plate), -c(cancel):")

                    if selection == "-a":
                        self._plate_service.display_menu()
                        plate_name = input("Enter new plate name:")
                        price = float(input("Enter new plate price:"))
                        self._plate_service.create_plate(plate_name, price)
                        self._plate_service.display_menu()

                    elif selection == "-r":
                        self._plate_service.display_menu()
                        plate_id = int(input("Enter the ID of plate to remove:"))
                        self._plate_service.delete_plate(plate_id)
                        self._plate_service.display_menu()

            elif selection == "-ma":

                while selection != "-c":
                    selection = input("-a(add admin account), -r(remove account), -c(cancel):")

                    if selection == "-a":
                        self._login_service.prompt_new_account_info(AccountType.ADMIN)
                    elif selection == "-r":
                        self._login_service.display_users()
                        delete_email = input("Enter email:")
                        self._login_service.delete_account(delete_email)
                        self._login_service.display_users()


