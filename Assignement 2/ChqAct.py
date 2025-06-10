from BaseClass import BankAccount

class CheckingAccount(BankAccount):

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        if self._balance - amount < 0:
            self._service_charges += 15
            print("Insufficient funds. $15 fee charged.")
            return

        super().withdraw(amount)

    def calc_interest(self):
        super().calc_interest()

    def close_month(self):
        self._service_charges += 5

        self._service_charges += self._num_withdrawals * 0.10

        super().close_month()