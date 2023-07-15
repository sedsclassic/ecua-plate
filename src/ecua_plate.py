from login import LoginService, AccountType
from plate import PlateService
from cart import CartService
from customer import CustomerService


login_service = LoginService()
plate_service = PlateService()

print("*************************************")
print("**            ECUA-PLATE!          **")
print("*************************************\n")


while True:
    login_service.display_users()

    selection = input("-l(log in), -s(sign up), -q(quit):")

    # Quit
    if selection == "-q":
        break

    # Log in
    elif selection == "-l":
        account_type = login_service.prompt_account_type()
        if login_service.login(account_type):

            plate_service.display_menu()

            # Customer
            cart_service = CartService(plate_service)
            customer_service = CustomerService(cart_service)
            customer_service.run_customer()

    # Sign up
    elif selection == "-s":
        account_type = login_service.prompt_account_type()
        login_service.register_account(account_type)
