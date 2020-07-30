import scrapy

import requests
import random
from time import sleep
import os.path

directory = 'C:/Katch_Media/web_scraping/SFUScript_Project/ScriptsDL/'

def saveFile(url, name, ext):
    print("Inside saveFile():")
    r = requests.get(url)
    print("R:" + r)
    print('\n\n\n\nDownloading ' + name +
          ' from ==> ' + url + ' ...\n\n\n\n')
    with open(directory + name + ext, 'wb') as f:
        f.write(r.content)

def sleepRandom():
    sleep(random.randint(1, 3))

def sleepRandomLong():
    sleep(random.randint(13, 30))

class MoviescriptSpider(scrapy.Spider):
    name = 'movieScript'
    allowed_domains = ['sfy.ru/']
    start_urls = ['https://sfy.ru/scripts?range=a']
    
    def parse(self, response):
        for tblNode in response.xpath('//div[@class = "container"]/div[@class = "row"]/div[@class = "two-thirds column"]/p')[:1]:
            movieName = tblNode.xpath('.//a/text()').extract_first()
            movieLink = tblNode.xpath('.//a/@href').extract_first()
            scriptLink = response.urljoin(movieLink)
            print("MovieName:" + movieName)
            print("MovieLink:" + movieLink)
            print("ScriptLink:" + scriptLink)
            sleepRandom()
            yield scrapy.Request(scriptLink, callback=self.dlScripts, meta={'movieName':movieName})


    def dlScripts(self, response):
        print("Inside dlScripts()")
        print("Inside dlScripts()")
        print("Inside dlScripts()")
        print("Inside dlScripts()")
        movieName = response.meta['movieName']
        movieLink = response.url
        extension = os.path.splitext(movieLink)[1]
        if extension != None:
            saveFile(movieLink, movieName, extension)