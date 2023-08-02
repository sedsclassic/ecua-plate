from dataclasses import dataclass
from enum import Enum
import string

# Admin password
ADMIN_PWD = "admin"
ADMIN_EMAIL = "admin@ecu.ec"


class AccountType(Enum):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'


@dataclass
class Account:
    name: string
    email: string
    password: string
    type: AccountType


class LoginService:
    _accounts: list[Account] = [
        Account("Admin", ADMIN_EMAIL, ADMIN_PWD, AccountType.ADMIN),
        Account("Jose Luis", "j@gmail.com", "joseluis", AccountType.CUSTOMER),
    ]

    def display_users(self):
        print("----------------USERS----------------")
        for acc in self._accounts:
            print(f"| {acc.name} {acc.email} {acc.type.value}")
        print("-------------------------------------\n")

    @staticmethod
    def request_admin_pwd():
        admin_pwd = input("Enter admin password:")
        if admin_pwd != ADMIN_PWD:
            print("Access denied.")
            return False
        return True

    def create_new_account(self, account_type: AccountType):
        if account_type == AccountType.ADMIN and not LoginService.request_admin_pwd():
            return

        name = input("Enter name:")
        email = input("Enter email:")

        for account in self._accounts:
            if account.email == email:
                print("An account already exists for that email.")
                return

        pwd1 = input("Enter password:")
        pwd2 = input("Confirm password:")
        if pwd1 != pwd2:
            print("Passwords do not match.")
            return

        self._accounts.append(Account(name, email, pwd2, account_type))
        print("Account added successfully.")

    def delete_account(self, email):
        if email == ADMIN_EMAIL:
            print("Denied.")
            return
        elif not LoginService.request_admin_pwd():
            return

        for acc in self._accounts:
            if acc.email == email:
                self._accounts.remove(acc)
                print("Account deleted successfully.")
                return
        print("Account not found.")

    def login(self, account_type: AccountType) -> bool:
        email = input("Enter email:")
        for acc in self._accounts:
            if email == acc.email and account_type == acc.type:
                pwd = input("Enter password:")
                if pwd == acc.password:
                    print(f"        Welcome {acc.name}!")
                    return True
                print("Incorrect password.")
                return False
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
