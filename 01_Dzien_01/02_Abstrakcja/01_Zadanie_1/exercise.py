import random


random_usdpln_rates = [3.5]
for _ in range(50):
    random_usdpln_rates.append(round(random_usdpln_rates[-1] + random.random() * 0.2 - 0.1, 2))


class CommandPrompt:
    def __init__(self, buy, sell, wait):
        self.buy = buy
        self.sell = sell
        self.wait = wait

    def ask(self):
        while True:
            choice = input('Decyzja [k/s/c/kup/sprzedaj/czekaj]: ')
            if choice not in self.buy and choice not in self.sell and choice not in self.wait:
                print(f'Niepoprawny wybór: {choice}')
            else:
                break
        if choice in self.buy:
            return 'buy'
        elif choice in self.sell:
            return 'sell'
        elif choice in self.wait:
            return 'wait'


command = CommandPrompt(('k', 'kup'), ('s', 'sprzedaj'), ('c', 'czekaj', ''))


class Wallet:
    def __init__(self, wallet_pln: float, wallet_usd: float):
        self.wallet_pln = wallet_pln
        self.wallet_usd = wallet_usd

    def convert_pln_to_usd(self, usdpln_rate):
        self.wallet_usd += self.wallet_pln / usdpln_rate
        self.wallet_pln = 0

    def convert_usd_to_pln(self, usdpln_rate):
        self.wallet_pln += self.wallet_usd * usdpln_rate
        self.wallet_usd = 0


def main(usdpln_rates):
    wallet = Wallet(100.0, 0.0)

    for usdpln_rate in usdpln_rates:
        print(f'Stan konta: {round(wallet.wallet_pln, 2)}zł, ${round(wallet.wallet_usd, 2)}, kurs {usdpln_rate}')
        choice = command.ask()
        if choice == 'buy':
            wallet.convert_pln_to_usd(usdpln_rate)
        elif choice == 'sell':
            wallet.convert_usd_to_pln(usdpln_rate)
        else:
            pass
    wallet.convert_usd_to_pln(usdpln_rates[-1])
    print(f'Twój wynik: {wallet.wallet_pln}zł!')


if __name__ == '__main__':
    main(random_usdpln_rates)
