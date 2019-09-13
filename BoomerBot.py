import pybomb
import tweepy
import json
import os
import random


def get_key(key):
    os.chdir("c:/users/bill/documents")
    secrets_filename = 'boomerkey.txt'
    with open(secrets_filename, 'r') as f:
        api_key = json.loads(f.read())
    return api_key[key]


def connect_giantbomb():
    key = get_key("GIANTBOMB")
    return pybomb.GamesClient(key)


def connect_twitter():
    auth = tweepy.OAuthHandler(get_key('TWITTER_API_KEY'), get_key('TWITTER_API_SECRET'))
    auth.set_access_token(get_key('TWITTER_ACCESS_TOKEN'), get_key('TWITTER_ACCESS_SECRET'))
    return tweepy.API(auth)


def random_date():
    year = random.randrange(1990, 2006)
    day = random.randrange(1,30)
    month = random.randrange(1, 12)
    return f"{year}-{day}-{month} 00:00:00"


def random_query():
    filter_by = {'platforms': pybomb.PC, 'original_release_date': random_date()}
    response = giantbomb.search(
        filter_by=filter_by,
        return_fields=('name', 'platforms', 'original_release_date'),
    )
    return response


twitter = connect_twitter()
giantbomb = connect_giantbomb()


while True:
    games = random_query()
    if len(games.results) > 0:
        #twitter.update_status(f"Yup, {games.results[0]['name']}, now THAT was a game.")
        twitter.update_status(f"Remember {games.results[0]['name']}? Man, those were the days.")
        break
