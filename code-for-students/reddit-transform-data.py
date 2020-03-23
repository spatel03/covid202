import requests
import json
from unidecode import unidecode


url = 'YOUR URL HERE!'
head = {'user-agent': 'NAME YOUR USER AGENT HERE!'}
redditdata = requests.get(url, headers=head).json()

# Make sure the lines above have accurate details in them from the first
# Reddit exercise.

# We have do drill down into the dictionary object to get access to the
# listings on Reddit -- the stuff we're really interested in.

# You probably don't need to change this.
listings = redditdata['data']['children']

# This is the iteration step that finally makes something appear! This is a
# "for loop" that FOR EACH item in the listings object that you created above
# prints the output of a function called unidecode. This is a tool that helps
# us deal with unicode characters such as special alphabetic characters and
# emoji.

for item in listings:
    print(unidecode(item['data']['title']))
