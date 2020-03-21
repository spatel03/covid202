import requests
import json
import pprint

# What?! I'l explain when we use it...
pp = pprint.PrettyPrinter(indent=4)

# Open this in IDLE script mode and save it as a new script.
# Follow along in class and fill in the details.
# Save this code for later! It should be helpful for future
# Studying and maybe your class project.

# STEP 1
# Get Reddit data by passing a URL and an element of an 
# HTTP GET request to the Python requests "get" function.

url = 'http://www.reddit.com/r/nba.json' # Make sure it's the "JSON version" of the URL!

head = {'user-agent': 'Warren Allen Test Code v0.1'}  # What does the User Agent do?

# You don't have to change this, but you do need to understand it!
# redditdata = requests.get(url)
redditdata = requests.get(url, headers=head).json()

# A new kind of object!
# print(type(redditdata))

# Fill in the details on the lines above and run the script.
# Then go to interactive mode to explore the data!


# Iterate over all of the titles of the listings
# and show each title on the terminal.


x = 0

###



###

for child in redditdata['data']['children']:
    try:
        print(child['data']['title'])
    except:
        print("error")
        pass

try:
    for child in redditdata['data']['children']:
        print(child['data']['title'])
except:
    print("error")
    pass










