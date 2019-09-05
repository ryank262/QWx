import requests
import xml.etree.ElementTree as ET

def parseXML(xmlFile):

   # create element tree object
   tree = ET.parse(xmlFile)

   # get root element 
   root = tree.getroot()

   print('\n' + root[0][8][0].text + '\n')
   discussion = root[0][8][2].text
   sections = discussion.split('&&')
   print(sections[0] + sections[1] + sections[2])

def main():

   URL = "https://www.wrh.noaa.gov/total_forecast/getprod.php?afos=xxxafdsgx&wfo=sgx&version=0&font=120&new=1&xml"

   response = requests.get(URL)



   with open('feed.xml', 'wb') as file:
      file.write(response.content)

   wxData = open('feed.xml', 'r')

   parseXML(wxData)

if __name__ == '__main__':
   main()
