import tweepy
import json
import pickledb
import csv
import pprint


def prnt(obj):
    """Retuns a pretty-printed version of an object."""
    pp = pprint.PrettyPrinter(indent=2)
    try:
        return(pp.pprint(obj))
    except:
        return("Problem with the printer!")


def extract(query):
    """Returns results from a Twitter search.
    
    Accepts one argument: the query (as a string object) to use to search Twitter."""
    
    if not isinstance(query, str):
        return None
    else:
        results = tw.search(query, tweet_mode="extended")
        return results


twconfig = {  # Twitter API configuration: Enter credentials here!
    'api_key': "",
    'api_secret': "",
    'access_token': "",
    "access_secret": ""
}

# Tweepy setup
auth = tweepy.OAuthHandler(
    twconfig['api_key'],
    twconfig['api_secret'])

auth.set_access_token(
    twconfig['access_token'],
    twconfig['access_secret'])

tw = tweepy.API(auth)
