from dataclasses import dataclass
from enum import Enum
import string

# Admin password
ADMIN_PWD = "admin"


class AccountType(Enum):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'


@dataclass
class Account:
    name: string
    email: string
    type: AccountType


class LoginService:
    _accounts: list[Account] = [
        Account("Aaa Aa", "a@a.a", AccountType.CUSTOMER),
        Account("Maria Jose", "majo@hotmail.com", AccountType.ADMIN),
        Account("Jose Maria", "joma@hotmail.com", AccountType.CUSTOMER),
    ]

    def display_users(self):
        print("----------------USERS----------------")
        for acc in self._accounts:
            print(f"| {acc.name} {acc.email} {acc.type.value}")
        print("-------------------------------------\n")

    @staticmethod
    def validate_admin_pwd():
        admin_pwd = input("Enter admin password:")
        if admin_pwd != ADMIN_PWD:
            print("Access denied.")
            return False
        return True

    def register_account(self, account_type: AccountType):
        if account_type == AccountType.ADMIN and not LoginService.validate_admin_pwd():
            return

        new_name = input("Enter your name:")
        new_email = input("Enter your email:")

        self._accounts.append(Account(new_name, new_email, account_type))
        print("Account added successfully.")

    def login(self, account_type: AccountType) -> bool:
        if account_type == AccountType.ADMIN and not LoginService.validate_admin_pwd():
            return False

        email = input("Enter email: ")
        for acc in self._accounts:
            if email == acc.email and account_type == acc.type:
                print(f"        Welcome {acc.name}!")
                return True
        print("Account not found.")
        return False

    @staticmethod
    def prompt_account_type() -> AccountType:
        user_type = ""
        while user_type != "-c" and user_type != "-a":
            user_type = input("-c(customer), -a(admin):")

        if user_type == "-c":
            return AccountType.CUSTOMER
        else:
            return AccountType.ADMIN


# login = LoginService()
# login.display_users()
# print("\n")
# login.add_user("Jema Lay", "jelay@uwa.ca", 'CUSTOMER')
# login.display_users()
# login.login()