import scrapy
from scrapy.loader import ItemLoader
from nurolbank.items import Article
from itemloaders.processors import TakeFirst

class NurolSpider(scrapy.Spider):
    name = 'nurol'
    allowed_domains = ['nurolbank.com.tr']
    start_urls = ['https://www.nurolbank.com.tr/bizdenhaberler.php?b=Nurolbank-Sosyal-Sorumluluk-Projeleri-&haber=1']

    def parse(self, response):
        links = response.xpath('//div[@class="fl leftMenu"]//a/@href').getall()
        yield from response.follow_all(links, self.parse_article, dont_filter=True)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//div[@class="fr menuContent"]/h1//text()').get()
        content = " ".join(response.xpath('//p[@class="lh20"]//text()').getall()).strip()

        item.add_value('title', title)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
