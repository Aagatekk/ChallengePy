from wallet import Wallet
from typing import Tuple


class Wizard:
    def __init__(self, name: str, age: float):
        self.name = name
        self.age = age
        #self.wallet = wallet

    #harrys_wallet = Wallet("Harry’s multi-currency wallet", {'GBP': 100, 'EUR': 80})
    #new_gbp_balance = harrys_wallet.display_balances()

    def give_money(self, money_to: "Wizard", amount, currency) -> Tuple[int, int]:
        if self.wallet.balances[currency] - amount >= 0:
            self.wallet.balances[currency] -= amount
            money_to.wallet.balances[currency] += amount
            print(self.wallet.balances[currency])
            print(money_to.wallet.balances[currency])
            return self.wallet.balances[currency], money_to.wallet.balances[currency]
        else:
            return -1, -1








#Give your character a `give_money()` method, which takes another character as an argument, together with
# a currency and an amount. The method should transfer that amount of currency (if available) from your character’s wallet
# to the other character’s wallet, using the appropriate Wallet methods.

