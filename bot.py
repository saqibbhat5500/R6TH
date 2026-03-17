import snscrape.modules.twitter as sntwitter
import requests
import time

BOT_TOKEN = "8783138970:AAFixrBvnmnniDLIxM3tkcvqysmPXV3SBz4"
CHAT_ID = "8799810283"

users = ["elonmusk", "realDonaldTrump", "Cristiano"]
keywords = ["coin", "token", "crypto", "contract", "CA"]

checked = set()

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

while True:
    try:
        for user in users:
            for tweet in sntwitter.TwitterUserScraper(user).get_items():
                if tweet.id in checked:
                    continue

                checked.add(tweet.id)

                if any(k in tweet.content.lower() for k in keywords):
                    send(f"🚨 {user} posted:\n\n{tweet.content}")

                break

        time.sleep(60)

    except Exception as e:
        print(e)
        time.sleep(30)
