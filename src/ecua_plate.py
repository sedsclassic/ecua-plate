from login import LoginService, AccountType
from plate import PlateService
from cart import CartService


login_service = LoginService()
plate_service = PlateService()

print("*************************************")
print("**            ECUA-PLATE!          **")
print("*************************************\n")


while True:
    login_service.display_users()

    selection = input("-l(log in), -s(sign up):")

    # Log in
    if selection == "-l":
        if login_service.login():
            # Add to cart
            plate_service.display_menu()
            cart_service = CartService(plate_service)
            plate_id = int(input("Enter ID to add plate:"))
            quantity = int(input("Enter quantity:"))
            cart_service.add_plate(plate_id, quantity)
            cart_service.display_cart()

    # Sign up
    elif selection == "-s":
        user_type = ""
        while user_type != "-c" and user_type != "-a":
            user_type = input("-c(customer), -a(admin):")

        if user_type == "-c":
            user_type = AccountType.CUSTOMER
        else:
            user_type = AccountType.ADMIN

        new_name = input("Enter your name:")
        new_email = input("Enter your email:")
        login_service.add_user(new_name, new_email, user_type)



