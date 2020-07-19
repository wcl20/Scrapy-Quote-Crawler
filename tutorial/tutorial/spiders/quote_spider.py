import scrapy
from dataclasses import dataclass

@dataclass
class Quote:
    text: str
    author: str
    tags: [str]

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = "http://quotes.toscrape.com/"
        # Get tag from cmd argument
        tag = getattr(self, "tag", None)
        if tag is not None:
            url += "tag/" + tag
        yield scrapy.Request(url, callback=self.parse)

    # Default callback to each url request
    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            text = quote.xpath("descendant::*[@class='text']/text()").get().strip(u'\u201c\u201d')
            author = quote.xpath("descendant::*[@class='author']/text()").get()
            tags = quote.xpath("descendant::*[@class='tag']/text()").getall()
            yield(Quote(text=text, author=author, tags=tags))

        # Follow links to next page
        links = response.xpath("//li[@class='next']/a")
        yield from response.follow_all(links, self.parse)
