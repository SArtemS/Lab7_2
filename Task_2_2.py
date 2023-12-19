from threading import Lock


class BankThread():

    def __init__(self, money=0):
        self._money = money
        self._lock = Lock()

    def deposit(self, addedMoney):
        with self._lock:
            self._money += addedMoney
            print(
                f'You deposited {addedMoney}\nCurrent balance: {self._money}\n'
            )

    def withdraw(self, removedMoney):
        with self._lock:
            if removedMoney > self._money:
                print(f'You withrawn {removedMoney}\nNot enough money!')
                print(f'Current balance: {self._money}\n')
            else:
                self._money -= removedMoney
                print(
                    f'You withrawn {removedMoney}\nCurrent balance: {self._money}\n'
                )
