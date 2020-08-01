import scrapy

import requests
import random
from time import sleep
import os.path

directory = 'C:/webscraping_simply/ScriptsDL/'

def saveFile(url, name, ext):
    r = requests.get(url)
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
    allowed_domains = ['simplyscripts.com']
    start_urls = ['https://www.simplyscripts.com/a.html']

    def parse(self, response):
        for tblNode in response.xpath('//div[@id = "blog"]/div[@id = "wrapper"]/div[@id = "wrapperleft"]/div[@id = "mainros"]/div[@id = "movie_wide"]/table/tbody/tr/td')[5:7]:
        #for tblNode in response.xpath('//*[@id="movie_wide"]/table/tbody/tr[3]/td[1]/a'):  
            print("inside for")
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
        movieName = response.meta['movieName']
        movieLink = response.url
        extension = os.path.splitext(movieLink)[1]
        if extension != None:
            saveFile(movieLink, movieName, extension)