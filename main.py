import requests
from bs4 import BeautifulSoup
from constants import BASE_URL, AD_ITEM_CLASS, RESULT_FNAME
from helpers import getAdContent, writeAdContentToFile

req = requests.get(BASE_URL)
soup = BeautifulSoup(req.text, features="lxml")
ads = soup.findAll('div', AD_ITEM_CLASS)

last_floor_apartments = []

def print_ad_content(data):
  text, address, url = data
  print(f'{text}, {address}\n{url}\n')

def print_regular_apartments():
  for ad in ads:
    text, address, url, last_floor = getAdContent(ad)

    if (last_floor == True):
      last_floor_apartments.append(ad)

def print_last_floor_apartments():
  for ad in last_floor_apartments:
    text, address, url, last_floor = getAdContent(ad)
    print_ad_content([text, address, url])
    writeAdContentToFile(f, [text, address, url])

with open(RESULT_FNAME, encoding='utf-8', mode="w") as f:
  f.write(f'Fetching from: {BASE_URL}\n\n')
  print_regular_apartments()
  print_last_floor_apartments()
