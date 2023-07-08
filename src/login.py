from dataclasses import dataclass
from enum import Enum
import string


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

    def add_user(self, name: string, email: string, acc_type: AccountType):
        self._accounts.append(Account(name, email, acc_type))
        print("Account added successfully.")

    def login(self) -> bool:
        email = input("Enter email: ")
        for acc in self._accounts:
            if email == acc.email:
                print(f"Welcome {acc.name}")
                return True
        print("Account not found.")
        return False

# login = LoginService()
# login.display_users()
# print("\n")
# login.add_user("Jema Lay", "jelay@uwa.ca", 'CUSTOMER')
# login.display_users()
# login.login()