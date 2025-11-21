import requests

url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    bitcoin_price = data['bitcoin']['usd']

    print(f"Current Bitcoin price: ${bitcoin_price} USD")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.ConnectionError:
    print("Error: Network problem (e.g., DNS failure, refused connection)")
except requests.exceptions.Timeout:
    print("Error: Request timed out")
except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
except KeyError:
    print("Error: Unexpected API response structure")
