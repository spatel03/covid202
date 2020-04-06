# The Online-202 Final Project

This document describes the final project that you will do in the "emergency online" version of 202. **The document will be updated as we go, so it will not reflect the full project until around week 14.**

To give you an idea of where this goes so that you can start your project planning right away, the final project will consist of three components:

1. The description of your project; specifically, the question you are using as the basis of your project, and the data you will use to answer the question.
2. A recorded walkthrough of the code you wrote as if you were presenting it to an interviewer for a job. An example and instructions will be posted.
3. The code itself, including informative in-code commenting.

## Recommended Packages/Data Sources

You will use a Web-based data API to extract, transform, and load data using Python. You should start to learn the basics of your API right away. What basics?

- How do you access it with Python?
- What are the rate limits or other factors that might get in the way?
- Where is the data you need for the question you have? _Is the data you need even available?!_

I am willing to help you in your explorations, but this research is indeed part of your project! So I won't supply all of the answers, and not just because I don't have all the answers.

You have three options for which API to use:

### 1\. Twitter Data

The recommended library to access Tweets (and other twitter data) is [Tweepy.](http://docs.tweepy.org/en/latest/) You will need a developer key for the Twitter API.

### 2\. Reddit Data

The recommended library to access Reddit is [PRAW](https://praw.readthedocs.io/en/latest) (the Python Reddit API Wrapper) which requires a developer key. Most student projects I've seen that use Reddit data (in fact, I think all of them) have successfully used the "add .json to a URL" method, which does not require a key. The best way for me to help you navigate this question is to identify your final project idea as early as possible.

### 3\. Other Web API

There are many, many data sources out there that you could use for this project. Here are just a few:

- [IMDB](https://imdbpy.readthedocs.io/en/latest/)
- [The Pokemon API](https://pokeapi.co/)
- [The last.fm music data API](https://www.last.fm/api)
- [The Spotify API](https://developer.spotify.com/documentation/web-api/)
- [MalShare](https://www.malshare.com/index.php) (a free Malware repository providing researchers access to samples, malicious feeds, and Yara results)
- [The GoodReads API](https://www.goodreads.com/api)
- [Data API from/about NPR](https://dev.npr.org/)
- A whole catalog of data from [The World Bank](https://datacatalog.worldbank.org/)
- [The Aztro horoscope API](https://aztro.readthedocs.io/en/latest/)
- [An API of Ice and Fire](https://anapioficeandfire.com/)
- [Clash of Clans Data API](https://developer.clashofclans.com)

**A warning about this option.** I don't want to scare you off of the idea of using data that interests you, but keep this in mind:

> I can only provide limited help with data sources that I don't already know. This includes troubleshooting (does the NASA API work? I've never used it, so I don't know) and answering questions about how to get data or what the data means (what even is a Pokeman? I have no idea.) There will be no extensions or exceptions given for this project, so as soon as possible make sure you know that a dataset works the way you think it works.
