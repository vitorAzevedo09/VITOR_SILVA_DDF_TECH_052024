import requests
import sys

import requests

api_key = sys.argv[1]
db_id = sys.argv[2]

url = f"https://maestro.dadosfera.ai/catalog/data-asset/{db_id}"

# Example payload
payload = {
    "name": "Online Retail II",
    "description": "This Online Retail II data set contains all the transactions occurring for a UK-based and registered, non-store online retail between 01/12/2009 and 09/12/2011.The company mainly sells unique all-occasion gift-ware. Many customers of the company are wholesalers.",
    "tags": [
        "retail", "e-commerce", "sales", "transactions", "customer behavior",
        "uk retail", "giftware", "wholesale", "time series", "revenue analysis",
        "product analysis", "customer segmentation",
        "marketing analytics", "sales performance", 
        "historical data"
    ],
}

headers = {
    "accept": "application/json",
    "dadosfera-lang": "en-us",
    "content-type": "application/json",
     "Authorization": f"{api_key}"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)
