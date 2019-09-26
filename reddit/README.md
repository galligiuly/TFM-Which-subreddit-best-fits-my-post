Links used:

http://www.storybench.org/how-to-scrape-reddit-with-python/
https://redditblog.com/2009/10/15/reddits-new-comment-sorting-system/
https://it.wikipedia.org/wiki/Reddit
https://redditblog.com/2019/07/29/the-benefits-of-machine-learning-to-study-small-dataset-of-social-conversations/

Dataset de Reddit
https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/

PRAW
https://github.com/praw-dev/praw/

Reddit data base
https://paperswithcode.com/search?q=reddit

NLP 
https://fasttext.cc/


Script Reddit with Python

How to access Reddit API to download data for my project.

Thinks we need:

1/ Reddit allow you to download his data trought an API, to do that we need to create an "app" within Reddid and get the OAuth2 keys to access the API.

2/ install these two pakages:
- Praw
- Pamdas

3/ if you don't have it, create a Reddit account

Let's start..


In the following page we can create (or create again) an app to connect to the API

https://www.reddit.com/prefs/apps

click on the bottom `are you a developer? create an app...`

fill up the form with you data and select the option `script`

My data:
    name: giuliagalli
    script
    description: script for my TFM
    redirect uri: http://localhost:80
    Create an app
    
Once you get the app created and saved your 14-character personal use script and 27-character secret key, we are ready to use the OAuth2 authorization to connect to the API and start scraping.


**Istanll PRAW package**

https://github.com/praw-dev/praw/

***Installing the Latest Development Version***

```bash
pip install --upgrade https://github.com/praw-dev/praw/archive/master.zip
```

***Installing Older Versions***

```bash
pip install praw==3.6.0
```

***Updating PRAW***

```bash
pip install --upgrade praw
```
















