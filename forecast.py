#!/usr/bin/env python

######
## Funny Console Forecast!
##         Powered by Yahoo API's
##
##          jmaillourbano@gmail.com
##
######

######
## Usage:
##      python forecast.py city
##      - or -
##      python forecast.py
##          -> city
######
import urllib3
import json
import certifi
import sys


## Starting
message = """#########
####
#### Funny forecast for Console
####
####        Powered by YahooApis
####
#########
"""
print(message)

baseurl = "https://query.yahooapis.com/v1/public/yql?q="

if len(sys.argv) < 2:
    location = input('Write location to check Forecast: ')
    queryjoin = "select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text='{}')".format(location)
else:
    queryjoin = "select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text='{}')".format(sys.argv[1])



# Joining strings
yql_url = baseurl + queryjoin + "&format=json"

print("\n# Retrieving data...\n")

#Connecting to Yahooapis
http = urllib3.PoolManager(
     cert_reqs='CERT_REQUIRED',
     ca_certs=certifi.where()
)
# Retrieving Informations
q = http.request('GET', yql_url )

# Saving information to JSON
results = json.loads(q.data)

# Printing results
title = results["query"]["results"]["channel"]["item"]["title"]
print(title, "\n")
for i in results["query"]["results"]["channel"]["item"]["forecast"]:
    #From Farenheit to Celsius
    celsiusMax = int(int(i["high"])-32)*5/9
    celsiusMin = int(int(i["low"])-32)*5/9
    print("- ",i['day'],i['date'], i['text'],"Max:", round(celsiusMax, 2),"Min:", round(celsiusMin, 2))
