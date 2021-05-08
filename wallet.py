from typing import Dict
import csv


class Wallet:

    def __init__(self, name: str):
        self.name = name
        self.balances: Dict[str, int] = {}

    def read_wallet_file(self) -> Dict[str, int]:
        try:
            with open(self.name.lower() + '_wallet.csv') as wallet_content:
                wallet = csv.reader(wallet_content)
                for row in wallet:
                    self.balances.update({row[0]: int(row[1])})
                return self.balances
        except FileNotFoundError:
            print("File not found. Aborting")

    def display_balances(self):
        print(self.balances)

    def save_balances(self):
        with open(self.name.lower() + '_wallet.csv', 'w', newline='') as wallet_content:
            writer = csv.writer(wallet_content)
            for key, value in self.balances.items():
                writer.writerow([key, value])

    def spend_money(self, currency: str, amount: int) -> int:
        if amount <= self.balances[currency]:
            self.balances[currency] = self.balances.get(currency, 0) - amount
            return self.balances[currency]
        else:
            return -1

    def deposit_money(self, currency: str, amount: int) -> int:
        self.balances[currency] = self.balances[currency] + amount
        return self.balances[currency]

