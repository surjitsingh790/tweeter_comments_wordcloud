from flask import render_template, request
from flask import Flask
import pandas as pd
import tweepy

app = Flask(__name__)
data = pd.read_csv('WC_Data.csv')
wlist = '-'.join([str(i) for i in data['Words']])
words = {'words_list': wlist}

@app.route('/')
def index():
    return render_template('./Main.html', data=words)

@app.route('/recollect', methods=['POST'])
def recollect():
    if request.method == 'POST':
        t = request.form['text']
        tweets_list = []

        api_key = "0Nfp0QdlOHXy5FVWtI8T7xdct"
        api_secret = "7IMXzjvfbStJejs1iI2B75esFcGehySRvWil31ZKGl48yNfr9E"
        access_token = "1354846100847550467-Lelq383ZqoVZDlRTyj9BfmVkWNyWyU"
        access_secret = "vqAMs6mi3oQpkwboh554koYc1e3ScEXbBdyGRqRV2E1Q5"

        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth)

        for tweet in tweepy.Cursor(api.search_tweets, q=t).items(20):
            tweets_list.append([tweet.text, tweet.created_at])

        recollected_tweets = {"tweets": tweets_list}

        return recollected_tweets


if __name__ == "__main__":
    app.run(debug=True)
