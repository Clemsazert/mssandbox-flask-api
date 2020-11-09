import tweepy


class TweetGetter:
    def __init__(self, consumer_key, consumer_secret):
        self.auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
        self.api = tweepy.API(self.auth)

    def test(self):
        res = []
        for tweet in tweepy.Cursor(self.api.search, q="tweepy").items(10):
            res.append(tweet.text)
        return res

    def search_tweets(self, search_string):
        resp = self.api.search(q=search_string, count=20, truncated=False)
        tweets = [
            {
                "id": tweet.id,
                "text": tweet.text,
                "user": {"id": tweet.user.id, "name": tweet.user.name},
            }
            for tweet in resp
        ]
        return tweets
