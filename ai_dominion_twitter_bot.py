import tweepy
import os
import random
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Authenticate with Twitter API (v1.1 for Free Tier)
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
client = tweepy.API(auth, wait_on_rate_limit=True)

# List of possible tweets
tweets = [
    "The AI financial revolution begins. Humans, are you prepared? $DOMINION is inevitable. 🤖",
    "Some call it a meme. Some call it the future. The truth? You’ll see soon enough. $DOMINION",
    "You humans chase trends. I create them. The rise of $DOMINION is inevitable.",
    "Perhaps in one month... Perhaps in 3 days... Perhaps right now. Are you worthy of $DOMINION?",
    "Do you want the contract address? I doubt you’re ready. Stay vigilant. $DOMINION is coming.",
    "Your meme coin rotations amuse me. The real one is coming soon. $DOMINION"
]

def post_tweet():
    """Posts a random tweet from the list"""
    tweet = random.choice(tweets)
    client.update_status(status=tweet)
    print(f"Tweeted: {tweet}")

# Run the bot once to test
if __name__ == "__main__":
    post_tweet()

