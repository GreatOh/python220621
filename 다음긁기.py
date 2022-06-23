# import requests
# import pprint

# url = "https://finance.daum.net/api/charts/A005930/days?limit=200&adjusted=true"

# headers = {
#     "referer": "https://finance.daum.net/chart/A005930",
#     "user-agent": "Mozilla/5.0"
# }

# params = {
#     "limit": "200",
#     "adjusted": "true"
# }

# resp = requests.get(url, headers=headers, params=params)
# data = resp.json()
# #pprint.pprint(data)
# data = data['data']

# for day in data:
#     print(day['date'], day['tradePrice'])

import requests
import pprint

url = "https://finance.daum.net/api/charts/A005930/days?limit=200&adjusted=true"

headers = {
    "referer": "https://finance.daum.net/chart/A005930",
    "user-agent": "Mozilla/5.0"
}

params = {
    "limit": "200",
    "adjusted": "true"
}

resp = requests.post(url,) .get(url, headers=headers, params=params)
data = resp.json()
#pprint.pprint(data)
data = data['data']

for day in data:
    print(day['date'], day['tradePrice'])