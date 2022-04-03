#This file is usefull to collect data from the Wikiloc web app
import sys
from urllib.request import Request, urlopen
import re
from grepfunc import grep

def getPageFromURL(url):
  req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
  webpage = urlopen(req).read().decode("utf-8")
  return webpage

def getRouteData(webpage):
  # Look for the interesting info in the webpage content
  dist_match = re.search("Distància<.p>\n\t+<span>\d+.\d*", webpage)[0]
  ps_match = re.search("Desnivell positiu<.p>\n\t+<span>\d+.\d*", webpage)[0]
  ns_match = re.search("Desnivell negatiu<.p>\n\t+<span>\d+.\d*", webpage)[0]
  time_match_try = re.search("Temps<.p>\n\t+<span> \d* \w* \d*", webpage)
  if time_match_try:
    time_match = time_match_try[0]
  else:
    return False
  # Obtain distance of the route
  distance = re.search("\d+,*\d*", dist_match)[0]
  distance = str(int(float(distance.replace(",", "."))*1000))

  # Obtain the possitive slope
  positive_slope = re.search("\d+\.*\d*", ps_match)[0]
  positive_slope = positive_slope.replace(".", "")

  # Obtain the negative slope
  negative_slope = re.search("\d+\.*\d*", ns_match)[0]
  negative_slope = negative_slope.replace(".", "")

  # Obtain and converting the time to minutes
  time = re.search("\d+ \w* \d*", time_match)[0]
  t = time.split(" hores ")
  if t[0].isnumeric():
    time = str(int(t[0]) * 60 + int(t[1]))
  else:
    print(t[0])
    return False
  # Concatenate all the data
  data = '%s %s %s %s\n' %( distance, positive_slope, negative_slope, time)
  return data

def writeData(data):
  # Add the data to the data.txt file if it's necessary
  f = open('data.txt', 'r+')
  if not(re.search(data, f.read())):
    f.write(data)
    print("Added line: %s" % data)
  else:
    print("That route is already in the file")
  f.close()

def getRouteList(webpage):
  url_match = re.findall("h2 class=\"trail__title\">\n\t+<a href=\"/rutes-senderisme/.+\"", webpage)

  url_list = []
  for url in url_match:
    url_list.append("https://ca.wikiloc.com%s" % url[45:-1])
  return url_list

def main():
  # Receive the url from the arguments and download the html file in string format
  url = sys.argv[1]

  webpage = getPageFromURL(url)
  url_list = getRouteList(webpage)
  for route_url in url_list:
    route_page = getPageFromURL(route_url)
    route_data = getRouteData(route_page)
    if route_data != False:
      writeData(route_data)

main()
