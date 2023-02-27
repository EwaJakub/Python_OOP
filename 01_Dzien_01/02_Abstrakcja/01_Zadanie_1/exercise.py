import random


random_usdpln_rates = [3.5]
for _ in range(50):
    random_usdpln_rates.append(round(random_usdpln_rates[-1] + random.random() * 0.2 - 0.1, 2))


def main(usdpln_rates):
    wallet_pln = 100.0
    wallet_usd = 0.0

    for usdpln_rate in usdpln_rates:
        print(f'Stan konta: {round(wallet_pln, 2)}zł, ${round(wallet_usd, 2)}, kurs {usdpln_rate}')
        while True:
            choice = input('Decyzja [k/s/c/kup/sprzedaj/czekaj]: ')
            if choice not in ('k', 's', 'c', 'kup', 'sprzedaj', 'czekaj', ''):
                print(f'Niepoprawny wybór: {choice}')
            else:
                break
        if choice in ('k', 'kup'):
            wallet_usd += wallet_pln / usdpln_rate
            wallet_pln = 0
        elif choice in ('s', 'sprzedaj'):
            wallet_pln += wallet_usd * usdpln_rate
            wallet_usd = 0

    wallet_pln += wallet_usd * usdpln_rate
    wallet_usd = 0
    print(f'Twój wynik: {wallet_pln}zł!')


if __name__ == '__main__':
    main(random_usdpln_rates)
