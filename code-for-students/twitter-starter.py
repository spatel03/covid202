import tweepy
import json
import pickledb
import csv
import pprint


def pprint(obj):
    """docstring"""
    pp = pprint.PrettyPrinter(indent=2)
    try:
        return(pp.pprint(obj))
    except:
        return("Problem with the printer!")


def extract(query):
    """docstring"""
    if not isinstance(query, str):
        return None
    else:
        results = tw.search(query, tweet_mode="extended")
        return results


def transform(tweet):
    """docstring"""
    # What do you want to do with your Tweet?


twconfig = {  # Twitter API configuration
    'api_key': "FOzwIQ8JD0WnqnSE3w2x4Fw99",
    'api_secret': "HRLsRUPcVneIpsXiZaC50pJ4zMbRPYY4vmWSgXryZHj9vRQo1w",
    'access_token': "16450742-pCmhIMf0Q98uuzk1cwsHtyxqrKlhAaW7gJbOIfDiH",
    "access_secret": "jaTAwTstKDz1HRIQNWvq0UlGqBodVlNsY0CtiNfx10ZhC"
}

# Tweepy setup
auth = tweepy.OAuthHandler(
    twconfig['api_key'],
    twconfig['api_secret'])

auth.set_access_token(
    twconfig['access_token'],
    twconfig['access_secret'])

tw = tweepy.API(auth)
