import requests
import json
from unidecode import unidecode

# STEP 1
# Get Reddit data by passing a URL and an element of an
# HTTP GET request to the Python requests "get" function.

# Where do you want to get data from? Also, make sure it's the "JSON version" of the URL!

url = 'YOUR URL HERE!'

# What does the User Agent do? Some Web services require this, others do not.
# In this particular case, Reddit does require it but it can be something
# fake like my example below.

head = {'user-agent': 'NAME YOUR USER AGENT HERE!'}

# Now let's create an object called redditdata. This object will contain the
# results of executing the code to the right of the "=". In this case, the get
# function from the requests library that we imported into this script is called.
# We pass it two arguments: the url variable, and a then a "headers" parameter
# to which we pass the head object we defined above. The results of the get
# function are also passed to the json() method, which will attempt to convert
# the results into a Python dictionary object.
#
# How would you know all this if you weren't in this class? The Requests
# documentation is very comprehensive and contains a great User Guide:
#
# https://requests.readthedocs.io/en/master/#the-user-guide

redditdata = requests.get(url, headers=head).json()

# If that all goes well then you can add code to access and manipulate the
# dict object you just created. You can also execute this code in IDLE script
# mode and then interact with the data in interactive mode.
