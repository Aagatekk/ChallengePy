from wizard import Wizard
from wallet import Wallet


class Main:

    harry = Wizard('Harry', 13)
    harrys_wallet = Wallet("Harry")
    harrys_wallet.read_wallet_file()
    harrys_wallet.display_balances()
    harrys_wallet.deposit_money('USD', 100000)
    harrys_wallet.display_balances()
    harrys_wallet.save_balances()
    harrys_wallet.display_balances()


    hermione = Wizard('Hermione', 13)
    #hermiones_wallet = hermione.wallet.read_wallet_file('Hermione')
    #print(harry.give_money(hermione, 150, 'USD'))
   # hermione.wallet.spend_money('USD', 20)
   # hermione.wallet.display_balances()
   # hermione.wallet.deposit_money('GBP', 300)
  #  hermione.wallet.display_balances()

