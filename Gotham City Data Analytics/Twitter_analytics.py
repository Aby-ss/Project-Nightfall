import tweepy
from rich import print

# Twitter API credentials
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def search_tweets(query, count=10):
    tweets = []
    try:
        # Retrieve tweets matching the query
        tweets = api.search(q=query, count=count, lang="en", tweet_mode="extended")
    except tweepy.TweepError as e:
        print(f"[bold red]Error:[/bold red] {str(e)}")
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