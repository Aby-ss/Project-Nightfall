import tweepy
from rich import print

# Twitter API credentials
API_KEY = "8biEytoyZzYW9Pcytm5TThQF7"
API_SECRET = "HDX6HQ5fDkHvMwNShsanfOCVcYa7cRhr23tBzgZ46n1dQMrEVr"
ACCESS_TOKEN = "1674187667553284097-pSD6kNKthu3h5YBbFizPhFUiqEop94"
ACCESS_TOKEN_SECRET = "IzJQwOcQHLLQ3cc6Lxn9tjrpTiBETUFWazSKg8y8Mtf3o"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def search_tweets(query, count=10):
    # Retrieve tweets matching the query
    tweets = api.search_tweets(q=query, lang="en", tweet_mode="extended", count=count)
    return tweets

def analyze_sentiment(tweet):
    # Perform sentiment analysis here (e.g., using a library like NLTK or TextBlob)
    # You can replace this placeholder implementation with your own sentiment analysis code
    return "Positive" if len(tweet) % 2 == 0 else "Negative"

def main():
    query = input("Enter a topic or hashtag to search for: ")
    count = int(input("Enter the number of tweets to retrieve: "))

    print()
    print(f"Searching for tweets related to '{query}'...")
    tweets = search_tweets(query, count)

    print()
    for tweet in tweets:
        username = tweet.user.screen_name
        created_at = tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
        text = tweet.full_text
        sentiment = analyze_sentiment(text)

        print(f"[bold]{username}[/bold] ({created_at})")
        print(text)
        print(f"Sentiment: [bold]{sentiment}[/bold]")
        print()

if __name__ == "__main__":
    main()