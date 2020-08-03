import scrapy

import requests
import random
from time import sleep
import os.path

directory = 'C:/Katch_Media/web_scraping/MovieScript_Project/ScriptsDL/'

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
    allowed_domains = ['dailyscript.com']
    start_urls = ['http://www.dailyscript.com/movie.html',
                  'http://www.dailyscript.com/movie_n-z.html']

    def parse(self, response):
        tableNodes = response.css('table ul p')
        for tblNode in tableNodes[:1]:
            movieName = tblNode.css('a::text').extract_first()
            movieLink = tblNode.css('a::attr(href)').extract_first()
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