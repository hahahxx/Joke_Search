import scrapy
import re
from joke.items import JokeItem
class JokeSpider(scrapy.Spider):
    name = "joke"
    allowed_domains = ["haha365.com"]
    start_urls = [
        "http://www.haha365.com/joke/index_10.htm"
    ]

    def parse(self, response):
        base_url = "http://www.haha365.com/joke/index_"
        for i in range(4005)[1:]:
            url = base_url + str(i) +  ".htm"
            yield scrapy.Request(url, callback=self.parse_single_page)

    def parse_single_page(self, response):
        filename = response.url.split("/")[-2]
        titles = response.xpath('//div/h3/a/text()').extract()
        contents = response.xpath('//div[@class="cat_llb"]')

        for content in contents:
            for i in [0,1]:
                if content.xpath( './/h3/a/text()' ).extract() and content.xpath( './/h3/a/text()' ).extract()[i]:
                    new_joke = JokeItem()
                    if content.xpath( './/div[@id="endtext"]' ).extract()[i]:
                        new_joke['title'] = content.xpath( './/h3/a/text()' ).extract()[i].encode('utf8')

                        raw_content = content.xpath( './/div[@id="endtext"]' ).extract()[i].encode('utf8')
                        new_content = re.sub('\<.*?\>','', raw_content).replace("\r","").replace("\n","")
                        new_joke['content'] = new_content
                        print new_joke['title']
                        print new_joke['content']
                        yield new_joke
