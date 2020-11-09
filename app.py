from flask import Flask
from flask_cors import CORS
from src.tweet_getter import TweetGetter
import os

# ------------------------------- App Instance ------------------------------ #

app = Flask(__name__)
CORS(app)

# Instances
getter = TweetGetter(
    os.environ.get("CONSUMER_KEY"), os.environ.get("CONSUMER_SECRET_KEY")
)

# -------------------------------- API Routes ------------------------------- #


def _format_error_message(message, code, dev_message=""):
    return {
        "status": code,
        "userMessage": message,
        "developerMessage": dev_message,
    }, code


@app.route("/healthcheck", methods=["GET"])
def hello_world():
    return {"status": "up", "version": "0.0.1", "environment": "development"}


@app.route("/test", methods=["GET"])
def testTweets():
    try:
        tweets = getter.test()
        return {"tweets": tweets}
    except Exception as e:
        return _format_error_message("An error occured", 500, str(e))


@app.route("/tweets/<search_string>")
def searchTweets(search_string):
    try:
        result = getter.search_tweets(search_string)
        return {"tweets": result}
    except Exception as e:
        return _format_error_message("An error occured", 500, str(e))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
