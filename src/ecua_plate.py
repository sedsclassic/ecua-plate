from login import LoginService
from plate import PlateService

login_service = LoginService()
plate_service = PlateService()

#Test
login_service.add_user("Jema Lay", "jelay@uwa.ca", 'CUSTOMER')

print("WELCOME TO ECUA-PLATE!")


while True:
    login_service.display_users()

    selection = input("-l(log in), -s(sign up):")

    if selection == "-l":
        if login_service.login():
            plate_service.display_menu()

    elif selection == "-s":
        user_type = ""
        while user_type != "-c" and user_type != "-a":
            user_type = input("-c(customer), -a(admin):")

        if user_type == "-c":
            user_type = 'CUSTOMER'
        else:
            user_type = 'ADMIN'

        new_name = input("Enter your name:")
        new_email = input("Enter your email:")
        login_service.add_user(new_name, new_email, user_type)



