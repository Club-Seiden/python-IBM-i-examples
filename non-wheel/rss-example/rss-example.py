#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser
from sys import argv

url = 'http://ibmsystemsmag.com/CMSTemplates/IBMSystemsMag/Feeds/Open-Your-i.aspx'
if len(argv) > 1:
    url = argv[1]

feed = feedparser.parse(url)

for entry in feed['entries'][:5]:
    print("\"{e[title]}\"\n{e[link]}\n".format(e=entry))

