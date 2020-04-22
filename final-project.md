# The Online-202 Final Project

This document describes the final project that you will do in the "emergency online" version of 202. At the end, you will submit the following:

**One Markdown document containing the following:**

1. A description of your project; specifically, the question you are using as the basis of your project, and the data you will use to answer the question.
2. A walkthrough of the code you wrote as if you were preparing it for an online portfolio of your work.
3. A summary of your results.
4. Some thoughts about what you would do next if this were a real-world project.
3. The complete script itself, minus any API key values.

**One video that confirms that your code executes successfully.** Why? There can be situations where a student's code runs in their environment but it does not run in mine. It will be too late to figure out what is wrong when I discover this issue. Therefore, as a safety measure, you must do a screen-recording of your code executing successfully. _The video does not have to be "professional" or "polished" it just has to be clear that it is your code and that it executes successfully._

**The actual script.** Name the file according to the following naming convention:

- firstnamelastname.py.txt (e.g., _warrenallen-final.py.txt_)

## How to submit your final project

Watch these videos for demonstrations of how to create the required document.

- [Final project report 1](https://youtu.be/tqTnlkiEOac)
- [Final project report 2](https://youtu.be/3Hb2Pi3TGJc)
- [Final project report 3](https://youtu.be/wka9LEhUaDA)

You will use these resources (described in the videos) to complete the final project report.

- [Carbon](https://carbon.now.sh)
- [StackEdit](https://stackedit.io)
- [imgbb.com](imgbb.com) or a comparable image hosting platform
- The final project report [markdown template](./final-report-md-template.md)

## Having trouble getting data? Want to reconsider your plans for the final project?

Once students really start working on their project, many realize that they waited too long to collect the data they need or that the data they thought they could retrieve cannot actually be retrieved. If you're in this situation -- or if you'd just rather change your research question to make use of this data -- you might consider using the COVID-19 Twitter dataset described below.

I've been collecting Tweets related to the COVID-19 pandemic since late January. I am making available to you a sample of that database for your project. There are a total of 1 million tweets (out of roughly 15 million) in this database. You can use this as a data source instead of the Twitter API, but the rest of the project (e.g., transforming and loading the Tweets) is the same as if you got the Tweets from directly from Twitter.

You'll need some starter code and a little bit of instruction. Here it is:

- [Video: How to access Dr. Allen's COVID-19 Tweets DB](https://youtu.be/ZgXeWvh6Nio)
- [Starter code](code-for-students/coviddb.py) (password for DB is in the video)
- [One example Tweet](code-for-students/example-tweet.txt)
- [One example Retweet](code-for-students/example-tweet.txt)

---

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
