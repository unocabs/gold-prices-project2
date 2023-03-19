import requests
from datetime import date
from datetime import timedelta
import pandas as pd
from forex_python.converter import CurrencyRates

c = CurrencyRates()

peso_rate = c.get_rate("USD", "PHP")

headers = {"x-access-token": "goldapi-244rlffq3gx0-io",
"Content-Type": "application/json"
}

data_list = []

try:
        for get_day in range(15, 0, -1): #range is for 15 days
            get_date  = date.today() - timedelta(days = get_day)
            date_entered = get_date.strftime("%Y%m%d")

            url = f"https://www.goldapi.io/api/XAU/USD/{date_entered}"
            response = requests.get(url, headers=headers)
            data = response.json()

            if response.status_code == 200:
                data_list.append([data['date'], data['price'] * peso_rate, data['price_gram_24k'] * peso_rate, data['price_gram_18k'] * peso_rate])
            else:
                print("Error fetching data from API")
except:
    pass

df = pd.DataFrame(data_list, columns = ["Date", "Trading Price", "Price per Gram 24K", "Price per Gram 18K"])

print(df)

df.to_excel("gold_prices.xlsx", index = False)

