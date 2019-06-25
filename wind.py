
#!/usr/bin/python
import requests
import xml.etree.ElementTree as ET
import sys

TEMP = 0
WIND_DIR = 4
WIND_SPD = 5
WIND_GST = 6

def parseXML(xmlFile, compare, more):

   a = 0
   b = 96
   d = 15

   if(more):
      d = 30  

   # create element tree object
   tree = ET.parse(xmlFile)

   # get root element 
   root = tree.getroot()

   for x in range(a, a + d):
      obsv = root[x]
      time = obsv.attrib['time'] 
      temp = obsv[TEMP].attrib['value']
      windDir = obsv[WIND_DIR].attrib['value']
      windSpd = obsv[WIND_SPD].attrib['value']
      gust = obsv[WIND_GST].attrib['value']
      #print(time, temp, windDir, windSpd + ' G' + gust)
      if(float(windSpd) > 100):
      	windDir = ''
      	windSpd = 'CALM'
      	gust = ''
      	print(f'{time:18}{temp:8}{windDir:4}{windSpd:4} {gust:2}')
      else:
      	print(f'{time:18}{temp:8}{windDir:6}{windSpd:2} G{gust:2}')

   if(compare):
      print('Yesterday:\n--------------------------------------')
      for x in range(b, b + d):
         obsv = root[x]
         time = obsv.attrib['time'] 
         temp = obsv[TEMP].attrib['value']
         windDir = obsv[WIND_DIR].attrib['value']
         windSpd = obsv[WIND_SPD].attrib['value']
         gust = obsv[WIND_GST].attrib['value']
         #print(time, temp, windDir, windSpd + ' G' + gust)
         if(float(windSpd) > 100):
            windDir = ''
            windSpd = 'CALM'
            gust = ''
            print(f'{time:18}{temp:8}{windDir:4}{windSpd:4} {gust:2}')
         else:
            print(f'{time:18}{temp:8}{windDir:6}{windSpd:2} G{gust:2}')

def main():

   #Del Mar
   URL = "https://www.wrh.noaa.gov/mesowest/getobextXml.php?sid=E9975&num=72"

   #Morro
   #URL = "https://www.wrh.noaa.gov/mesowest/getobextXml.php?sid=OX1MB&num=72"

   compare = False
   more = False

   for x in range(1, len(sys.argv)):
      if sys.argv[x] == "more":
         more = True
      elif(sys.argv[x] == "compare"):
         compare = True
      else:
         print("Usage: wind.py [more] | [compare]")
   

   response = requests.get(URL)

   print('\nDel Mar (17th St)\n')
   time = 'Time'
   tmp = 'Temp(F)'
   windDir = 'Wind (MPH)'
   print(f'{time:16}{tmp:11}{windDir:4}')
   print('--------------------------------------')



   with open('feed.xml', 'wb') as file:
      file.write(response.content)

   windData = open('feed.xml', 'r')

   parseXML(windData, compare, more)

if __name__ == '__main__':
   main()