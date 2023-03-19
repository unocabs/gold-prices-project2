import requests
from datetime import date
from datetime import timedelta

headers = {"x-access-token": "goldapi-244rlffq3gx0-io",
"Content-Type": "application/json"
}

try:
    scope_days = 30
    for get_day in range (4, 0, -1):
        get_date  = date.today() - timedelta(days = get_day)
        date_entered = get_date.strftime("%Y%m%d")

        url = f"https://www.goldapi.io/api/XAU/USD/{date_entered}"
        response = requests.get(url, headers = headers)
        data = response.json()

        if response.status_code == 200:
            data = response.json()
            print(f"{data}")
        else:
            print("Error fetching data from API")
except:
    pass