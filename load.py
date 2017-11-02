import os, sys, time, telepot, unicodedata, urllib3, random, re
from telepot.loop import MessageLoop
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
from time import gmtime, strftime
from tabulate import tabulate

url = "http://penteli.meteo.gr/stations/neaperamos/"
req = urlopen(url)
page = req.read()
req.close()
page_soup = soup(page, "html.parser")
