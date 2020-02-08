import requests
from bs4 import BeautifulSoup

class WebScrapper():
   wikiDoc = requests.get("https://en.wikipedia.org/wiki/Main_Page");
   parsedDoc = BeautifulSoup(wikiDoc.content, "html.parser")

   def getTitle(self):
     title = self.parsedDoc.title.string
     return title

   def getWikiLinks(self):
       list =[]
       for link in self.parsedDoc.find_all('a'):
           list.append(link.get('href'))
       return list

webs = WebScrapper()
print(webs.getTitle())
print(webs.getWikiLinks())