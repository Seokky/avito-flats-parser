import re

""" Public """

def writeAdContentToFile(f, data):
  text, address, url = data
  f.write(f'{text} {address}\n')
  f.write(f'{url}\n\n')


def getAdContent(ad):
  text, address, url = __parseAdContent(ad)

  return [
    __formatAdText(text),
    __formatAdAddress(address),
    __formatAdUrl(url),
    __isThatLastFloorAparts(text)
  ]

""" Private """

def __parseAdContent(ad):
  text = __parseAdText(ad)
  url = __parseAdUrl(ad)
  address = __parseAdAddress(ad)

  return [text, address, url]

def __parseAdText(ad):
  return ad.findAll('a', 'snippet-link')[0].text

def __parseAdUrl(ad):
  return ad.findAll('a', 'snippet-link')[0]['href']

def __parseAdAddress(ad):
  return ad.findAll('span', 'item-address__string')[0].text

def __isThatLastFloorAparts(ad_text):
  floors = re.findall(r"(\d+\/\d+\s)(эт.)", ad_text)[0][0]
  floor, max_floor = floors.split('/')
  return int(floor) == int(max_floor)

def __formatAdText(text):
  formatted = re.sub(r"(\d+\s)(м²,\s)", "", text)
  formatted = formatted.replace(' квартира', '')
  return formatted

def __formatAdUrl(url):
  return f'https://www.avito.ru{url}'

def __formatAdAddress(address):
  return address.strip()