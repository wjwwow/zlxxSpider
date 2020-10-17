# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZgzwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    a_number=scrapy.Field()
    a_day=scrapy.Field()
    p_number=scrapy.Field()
    p_day=scrapy.Field()
    applicant=scrapy.Field()
    address=scrapy.Field()
    inventor=scrapy.Field()
    code=scrapy.Field()
    abstract=scrapy.Field()
    principal=scrapy.Field()
    pages=scrapy.Field()
    m_number=scrapy.Field()
    c_number=scrapy.Field()
    agency=scrapy.Field()
    agent=scrapy.Field()




