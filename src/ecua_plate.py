from login import LoginService, AccountType
from plate import PlateService
from cart import CartService
from customer import CustomerService
from admin import AdminService


login_service = LoginService()
plate_service = PlateService()

print("*************************************")
print("**            ECUA-PLATE!          **")
print("*************************************\n")


selection = ""

while selection != "-q":  # Quit
    login_service.display_users()
    selection = input("-l(log in), -s(sign up), -q(quit):")

    # Log in
    if selection == "-l":
        account_type = login_service.prompt_account_type()
        if login_service.login(account_type):

            # Customer
            if account_type == AccountType.CUSTOMER:
                plate_service.display_menu()
                cart_service = CartService(plate_service)
                customer_service = CustomerService(cart_service)
                customer_service.run_customer()

            # Admin
            elif account_type == AccountType.ADMIN:
                admin_service = AdminService(login_service, plate_service)
                admin_service.run_admin()

    # Sign up
    elif selection == "-s":
        login_service.prompt_new_account_info(AccountType.CUSTOMER)
