import scrapy


class TestSpider(scrapy.Spider):
    name = 'testspider'
    start_urls = ['https://pages.coupang.com/p/84871']

    def parse(self, response):
        data = []
        items = response.css('.descriptions')  # ul.baby-product-list li em.sale strong.price-value::text
        for item in items:
            name = item.css('.name::text').get().strip()
            price = item.css('.price-value::text').get().strip()
            print(name + ' / ' + price + '원')

