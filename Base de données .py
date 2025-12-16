import requests
import pandas as pd
import time

API_KEY = "pub_19a494eec7654778a59510fd3aa995e3"  # créez une clé gratuite sur https://newsdata.io
tickers = ["MSFT", "NVDA",  "AAPL",
    "AMZN", "GOOGL", "GOOG", "META", "TSLA", "BRK-B", "AVGO",
    "JPM", "LLY", "V", "MA", "UNH", "XOM", "WMT", "COST", "HD","NFLX"]

all_articles = []

for ticker in tickers:
    print(f"--- Collecte des actualités pour {ticker} ---")
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&q={ticker}&language=en&category=business"
    
    try:
        r = requests.get(url)
        data = r.json()
        if "results" in data:
            for article in data["results"]:
                all_articles.append({
                    "Ticker": ticker,
                    "Title": article.get("title"),
                    "Description": article.get("description"),
                    "Date": article.get("pubDate"),
                    "Source": article.get("source_id")
                })
        time.sleep(2)  # éviter le throttling
    except Exception as e:
        print(f"Erreur pour {ticker}: {e}")

df_news = pd.DataFrame(all_articles)
df_news.dropna(subset=["Description"], inplace=True)
df_news.to_csv("financial_news.csv", index=False)
print(df_news.head())