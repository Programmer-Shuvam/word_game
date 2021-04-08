import scrapy
from scrapy.crawler import CrawlerProcess

dict = {
    'ROBOTSTXT_OBEY': False,
    'DOWNLOADER_MIDDLEWARES': {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400, },
    }

class wrd_scrpr(scrapy.Spider):
    name = 'yes'
    x = 'http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.'
    y = []
    data = []
    for i in range(1, 25):
        if len(str(i)) > 1:
            y.append(x + str(i))
        else:
            y.append(x + '0' + str(i))
    start_urls = y

    def parse(self, response):
        names = response.css('.co li::text').extract()
        self.data+=names
        
process = CrawlerProcess(settings=dict)
process.crawl(wrd_scrpr)
process.start()
wrd_scrpr.data.sort()

f=open('words.txt','a')
for i in wrd_scrpr.data:
    f.write(i+',')
f.close()
