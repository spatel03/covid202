import requests
import json
from unidecode import unidecode

my_app_name = "???"  # Change this to something meaningful.

def get_posts(subreddit):
    """Returns useful data about Reddit posts from a given subreddit.

    (Define more details later)
    """

    # Get the full Reddit listings object

    url = f'https://www.reddit.com/r/{subreddit}.json'
    head = {'user-agent': my_app_name}
    rawdata = requests.get(url, headers=head).json()
    
    # Return just the items of interest.
    
    listings = rawdata['data']['children']
    
    for item in listings:
        print(unidecode(item['data']['title']))
    


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

get_posts("news")
