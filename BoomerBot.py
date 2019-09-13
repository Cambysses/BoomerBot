import pybomb
import tweepy
import json
import os
import random


def get_key(key):
    # Gets API key from local file.
    os.chdir("c:/users/bill/documents")
    secrets_filename = 'boomerkey.txt'
    with open(secrets_filename, 'r') as f:
        api_key = json.loads(f.read())
    return api_key[key]


def connect_giantbomb():
    # Initiate connection to GB API.
    key = get_key("GIANTBOMB")
    return pybomb.GamesClient(key)


def connect_twitter():
    # Initiate connection to Twitter API.
    auth = tweepy.OAuthHandler(get_key('TWITTER_API_KEY'), get_key('TWITTER_API_SECRET'))
    auth.set_access_token(get_key('TWITTER_ACCESS_TOKEN'), get_key('TWITTER_ACCESS_SECRET'))
    return tweepy.API(auth)


def random_date():
    # Generates random date within range.
    year = random.randrange(1990, 2006)
    day = random.randrange(1,30)
    month = random.randrange(1, 12)
    return f"{year}-{day}-{month} 00:00:00"


def random_query():
    # Queries GB database for game title(s).
    filter_by = {'platforms': pybomb.PC, 'original_release_date': random_date()}
    response = giantbomb.search(
        filter_by=filter_by,
        return_fields=('name', 'platforms', 'original_release_date'),
    )
    return response


def main():
    twitter = connect_twitter()
    giantbomb = connect_giantbomb()

    # Loops until it finds a game, tweets using template.
    while True:
        games = random_query()
        if len(games.results) > 0:
            # twitter.update_status(f"Yup, {games.results[0]['name']}, now THAT was a game.")
            # twitter.update_status(f"Remember {games.results[0]['name']}? Man, those were the days.")
            break
