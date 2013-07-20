"""
new-wea.py - Phenny Weather Module using Dark Sky API
Copyright 2013, Jin Park - jinpark.net
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import urllib, simplejson, apikey, csv

degc = "\xc2\xb0C "
degf = "\xc2\xb0F "
forc = ['f','F','c','C']

def wf(phenny, input):
  """Displays weather using Dark Sky API"""
  userinput = str(input.group(2))
  #create dict to search for nick/location
  with open('nickloc.csv', 'rU') as f:
    z = csv.reader(f)
    nickdict = {}
    for key, val in z:
      nickdict[key] = val
  nickname1 = input.nick
  nickname2 = nickname1.strip().lower()
  if nickname2 in nickdict:
    if userinput in forc:
			loc = nickdict[nickname2] + " " + userinput
    elif userinput == 'None':
      loc = nickdict[nickname2]
    else:
    	loc = userinput
  else:
    loc = userinput
  if loc == 'None':
    urlunits = 'si' 
  elif loc[-2:] == " C" or loc[-2:] == " c":
    urlunits = 'si'
    loc = loc[:-2]
  elif loc[-2:] == " F" or loc[-2:] == " f":
    urlunits = 'us'
    loc = loc[:-2]
  else:
  	urlunits = 'si'
  locinput1 = loc.strip().lower().encode('utf8')
  htmlinput = urllib.quote(locinput1)
  # url2 = 'http://nominatim.openstreetmap.org/search?q=' + htmlinput + '&format=json'
  # jsonResponse = simplejson.load(urllib.urlopen(url2))
  # lati = jsonResponse[0]['lat']
  # longi = jsonResponse[0]['lon']
  # loca = jsonResponse[0]['display_name']
  url4 = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + htmlinput + '&sensor=true'
  jsonResponse1 = simplejson.load(urllib.urlopen(url4))
  longi = jsonResponse1['results'][0]['geometry']['location']['lng']
  lati = jsonResponse1['results'][0]['geometry']['location']['lat']
  loca = jsonResponse1['results'][0]['formatted_address']
  url3 = 'https://api.forecast.io/forecast/' + apikey.darksky + '/' + str(lati) + ',' + str(longi) + '?units=' + urlunits
  weajson = simplejson.load(urllib.urlopen(url3))
  currentwea = weajson['daily']['data'][0]
  tomwea = weajson['daily']['data'][1]
  units = weajson['flags']['units']
  if units == 'us':
    deg = degf
  else:
    deg = degc
  phennyout = loca.encode('utf8') + "\x02" + " Today: " + "\x02" + str(int(round(currentwea["temperatureMin"]))) + "\xc2\xb0/" + str(int(round(currentwea["temperatureMax"]))) + deg + currentwea["summary"] + "\x02" + " Tomorrow: " + "\x02" + str(int(round(tomwea["temperatureMin"]))) + "\xc2\xb0/" + str(int(round(tomwea["temperatureMax"]))) + deg + tomwea["summary"] + "\x02" + " This Week: " + "\x02" + weajson['daily']['summary'].encode('utf8')
  phenny.say(phennyout)



wf.commands = ['wf']
wf.priority = 'low'
wf.example = '.wf 11361'

def wea(phenny, input):
  """Displays weather using Dark Sky API"""
  userinput = str(input.group(2))
  #create dict to search for nick/location
  with open('nickloc.csv', 'rU') as f:
    z = csv.reader(f)
    nickdict = {}
    for key, val in z:
      nickdict[key] = val
  nickname1 = input.nick
  nickname2 = nickname1.strip().lower()
  if nickname2 in nickdict:
    if userinput in forc:
			loc = nickdict[nickname2] + " " + userinput
    elif userinput == 'None':
      loc = nickdict[nickname2]
    else:
    	loc = userinput
  else:
    loc = userinput
  if loc == 'None':
    urlunits = 'si' 
  elif loc[-2:] == " C" or loc[-2:] == " c":
    urlunits = 'si'
    loc = loc[:-2]
  elif loc[-2:] == " F" or loc[-2:] == " f":
    urlunits = 'us'
    loc = loc[:-2]
  else:
  	urlunits = 'si'
  locinput1 = loc.strip().lower().encode('utf8')
  htmlinput = urllib.quote(locinput1)
  # url2 = 'http://nominatim.openstreetmap.org/search?q=' + htmlinput + '&format=json'
  # jsonResponse = simplejson.load(urllib.urlopen(url2))
  # lati = jsonResponse[0]['lat']
  # longi = jsonResponse[0]['lon']
  # loca = jsonResponse[0]['display_name']
  url4 = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + htmlinput + '&sensor=true'
  jsonResponse1 = simplejson.load(urllib.urlopen(url4))
  longi = jsonResponse1['results'][0]['geometry']['location']['lng']
  lati = jsonResponse1['results'][0]['geometry']['location']['lat']
  loca = jsonResponse1['results'][0]['formatted_address']
  url3 = 'https://api.forecast.io/forecast/' + apikey.darksky + '/' + str(lati) + ',' + str(longi) + '?units=' + urlunits
  weajson = simplejson.load(urllib.urlopen(url3))
  nowwea = weajson['currently']
  units = weajson['flags']['units']
  if units == 'us':
    deg = degf
  else:
    deg = degc
  phennyout = loca.encode('utf8') + ": " + str(int(round(nowwea["temperature"]))) + deg + nowwea["summary"]
  phenny.say(phennyout)



wea.commands = ['wea']
wea.priority = 'low'
wea.example = '.wea 11361'