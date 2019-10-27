import scrapy


class QuotesSpider(scrapy.Spider):
    name = "aqual"
    start_urls = [
        'https://www.airlinequality.com/airline-reviews/jetblue-airways/',
    ]

    def parse(self, response):
       for body in response.css('div.body'):
           yield {
               'rating' :body.css('td::text').getall()[-1],
               'text': body.css("div.text_content::text").getall()[-1],
           }

       next_page= response.css('article.position- a::attr(href)').getall()[-1]
       if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
