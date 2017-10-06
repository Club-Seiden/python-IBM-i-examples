# Examples using feedparser on IBM i

This example fetches an RSS feed and prints the first 5 entries from it, showing the title of the entry and the link to that entry. If you do not specify a URL to an RSS feed, it will default to Jesse Gorzinski's "Open Your i" blog feed.

# Installing requisites
 - Make sure you have installed 5733OPS Option 2, along with PTFs SI59051, SI60563, SI60564, and SI61963 (or subsequent PTFs)!
   See [here](https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/IBM%20i%20Technology%20Updates/page/Python%20PTFs) for the latest PTF numbers.
 - ```pip3 install -r requirements.txt```

# Running the Examples
```python3 ./rss-example.py [url]```

# More Info

- feedparser [documentation](https://pypi.python.org/pypi/feedparser)