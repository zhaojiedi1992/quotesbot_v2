from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class QuotesToscrape(BasePortiaSpider):
    name = "quotes.toscrape.com"
    allowed_domains = [u'quotes.toscrape.com']
    start_urls = [u'http://quotes.toscrape.com/page/1']
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'/page/'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(PortiaItem,
                   None,
                   u'.quote',
                   [Field(u'desc',
                          '.text *::text',
                          []),
                       Field(u'author',
                             'span:nth-child(2) > .author *::text',
                             []),
                       Field(u'tag',
                             '.tags>.tag *::text',
                             [])])]]
