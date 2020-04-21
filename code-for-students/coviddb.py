from pymongo import MongoClient

# You can leave this alone. It connects you to the database.
client = MongoClient('161.35.53.173',
                     27017,
                     authSource='covid',
                     username='student',
                     password='')  # See the week 14 video for the password
db = client['covid']
covidtweets = db['tweets']


def search(query={}):
    """Searches Dr. Allen's COVID Tweets DB and returns a PyMongo cursor"""
    
    try:
        results = covidtweets.find(query)
    except:
        print("Could not execute query.")
        sys.exit()
    else:
        return results


def sample(samplesize=1):
    """Returns a random sample of tweets of the size past, or 1."""
    
    results = covidtweets.aggregate([{'$sample': {'size': samplesize}}])
    return results


# SEARCHING FOR TWEETS
# Pass a dict to define query or you'll search all 1mil tweets.
# Comment out the line below if you're using the sample method.
data = search()

# EXTRACT A RANDOM SAMPLE
# Pass an integer to select a random sample of that many tweets. There are
# exactly 1mil tweets in the database. Pass nothing to get one random
# tweet object, e.g., to explore the object manually to find the data you're
# looking for.
data = sample()
