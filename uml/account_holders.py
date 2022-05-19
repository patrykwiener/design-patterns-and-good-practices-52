from abc import ABC


class Account:
    def __init__(self, balance: float = 0.0):
        self._balance = balance

    def deposit(self, amount: float):
        pass

    def withdraw(self, amount: float):
        pass

    def get_balance(self) -> float:
        pass


class AccountHolder(ABC):
    def __init__(self, _id: int, email: str, accounts: list[Account]):
        self._id = _id
        self._email = email
        self._accounts = accounts


class IndividualHolder(AccountHolder):
    def __init__(self, _id: int, email: str, accounts: list[Account], name: str, pesel: str):
        super().__init__(_id, email, accounts)
        self._name = name
        self._pesel = pesel


class CorporateHolder(AccountHolder):
    def __init__(self, _id: int, email: str, accounts: list[Account], contact: str):
        super().__init__(_id, email, accounts)
        self._contact = contact


def delete_holder(holder, accounts):
    del accounts
    del holder


def main():
    accounts = [
        Account(15),
        Account(15000),
    ]
    holder = CorporateHolder(_id=1, email='a@a.com', accounts=accounts, contact='costam')

    del holder


if __name__ == '__main__':
    main()
