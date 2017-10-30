import os, sys, time, telepot, unicodedata, urllib3, random
from telepot.loop import MessageLoop
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
from time import gmtime, strftime
from tabulate import tabulate

TOKEN= os.environ['TOKEN']
#some_api_token = os.environ['SOME_API_TOKEN']
#r = redis.from_url(os.environ.get("REDIS_URL"))
#PORT = int(os.environ.get('PORT', '5000'))
#updater = Updater(TOKEN)
# add handlers
#updater.start_webhook(listen="0.0.0.0",
 #                     port=PORT,
  #                    url_path=TOKEN)
#updater.bot.set_webhook("https://meteokavgr.herokuapp.com/" + TOKEN)
#updater.idle()

def scrap():
    url = "http://penteli.meteo.gr/stations/neaperamos/"
    req = urlopen(url)
    page = req.read()
    req.close()
    page_soup = soup(page, "html.parser")
   # values_list = [
   # [page_soup.find_all("strong")[1].text.strip()+" "+page_soup.find_all("strong")[2].text.strip()]]
    #return tabulate(values_list)
    div = page_soup.find_all("strong")   
    #for value in div:
        #item =[]
        #item = value.text.strip()
        #return div
#tab
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(msg, content_type, chat_type, chat_id, strftime("%a, %d %b %Y %H:%M:%S +0000"))

    if content_type == 'text':
        bot.sendMessage(chat_id, div)


bot = telepot.Bot(TOKEN)
#some_api = some_api_lib.connect(some_api_token)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(120)

