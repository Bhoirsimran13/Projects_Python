import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.bbc.com/news'

response = requests.get(url)
if response.status_code == 200:
    print("Successfully fetched the web page.")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')

headlines = []
for item in soup.find_all('h2'):
    headline_text = item.get_text(strip=True)
    if headline_text:
        headlines.append(headline_text)

data = {'Headline': headlines}
df = pd.DataFrame(data)
df.to_csv('headlines.csv', index=False)

print(f"Scraped {len(headlines)} headlines and saved to 'headlines.csv'")
