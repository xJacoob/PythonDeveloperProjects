import requests
def curriencies_from_url(user_currency):
    currencies = requests.get(f"http://www.floatrates.com/daily/{user_currency}.json")
    return currencies.json()

def calculate(user_currency, cache, user_currency_exchange_rate, user_money):
    print("Checking the cache...")
    if user_currency_exchange_rate in cache:
        result = round(user_money * cache[user_currency_exchange_rate], 2)
        return f"Oh! It is in the cache!\nYou received {result} {user_currency_exchange_rate.upper()}"
    else:
        currencies = curriencies_from_url(user_currency)
        cache[user_currency_exchange_rate] = currencies[user_currency_exchange_rate]['rate']
        result = round(user_money * cache[user_currency_exchange_rate], 2)
        return f"Sorry, but it is not in the cache!\nYou received {result} {user_currency_exchange_rate.upper()}."

def main():
    user_currency_ = input().lower()
    values = curriencies_from_url(user_currency_)
    cache = {}
    if user_currency_ != "usd":
        cache['usd'] = values['usd']['rate']
    if user_currency_ != "eur":
        cache['eur'] = values['eur']['rate']
    while True:
        user_currency_exchange_ = input().lower()
        if user_currency_exchange_ == "":
            break

        user_money_ = float(input())
        result = calculate(user_currency_, cache, user_currency_exchange_, user_money_)
        print(result)


if __name__ == "__main__":
    main()


