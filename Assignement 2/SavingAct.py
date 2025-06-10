from BaseClass import BankAccount

class SavingsAccount(BankAccount): #call parent method

    def deposit(self, amount):
        super().deposit(amount)

        if not self._active and self._balance >= 25:
            self._active = True

    def withdraw(self, amount):
        if not self._active:
            print("Account is inactive. Withdrawal denied.")
            return

        super().withdraw(amount)

    def calc_interest(self):
        super().calc_interest()

    def close_month(self):
        if self._num_withdrawals > 4:
            extra_charges = (self._num_withdrawals - 4) * 1
            self._service_charges += extra_charges

        super().close_month()
# add parent method
