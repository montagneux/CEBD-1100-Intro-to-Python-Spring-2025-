from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, balance, interest_rate):
        self._starting_balance = 0.00
        self._balance = 0.00
        self._total_deposits = 0.00
        self._num_deposits = 0
        self._total_withdrawals = 0.00
        self._num_withdrawals = 0
        self._interest_rate = 0.00
        self._service_charges = 0.00
        self._active = True if balance >= 25 else False

    @abstractmethod
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be greater than zero.")
            return

        self._balance += amount
        self._num_deposits += 1
        self._total_deposits += amount

    @abstractmethod
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be greater than zero.")
            return

        self._balance -= amount
        self._num_withdrawals += 1
        self._total_withdrawals += amount

        if self._balance < 25:
            self._active = False

    @abstractmethod
    def calc_interest(self):
        monthly_rate = self._interest_rate / 12
        interest = self._balance * monthly_rate
        self._balance += interest

    @abstractmethod
    def close_month(self):
        self._balance -= self._service_charges

        self.calc_interest()

        self._starting_balance = self._balance
        self._num_deposits = 0
        self._num_withdrawals = 0
        self._service_charges = 0.00