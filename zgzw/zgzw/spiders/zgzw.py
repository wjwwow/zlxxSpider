from scrapy.spiders import Spider
import time

import scrapy


#导入定义的item
from ..items import ZgzwItem
import requests

class zgzwSpider(Spider):
    # response=requests.get('http://httpbin.org/get')
    # print(response.text)
    name = 'zgzw'  #爬虫名称
    allowed__domains=['dbpub.cnki.net']  #爬虫请求的域名
    s=0
    offset=str(s).zfill(5)

    start_urls = ['https://dbpub.cnki.net/grid2008/dbpub/detail.aspx?dbcode=SCPD&dbname=SCPD2023&filename=CN104600000A']


    custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    #         'zgzw.middlewares.ProcessAllExceptionMiddleware': 120,
    #         'zgzw.middlewares.SimpleProxyMiddleware': 100
    #     },
        'AUTOTHROTTLE_START_DELAY':0.2, # 延时最低为2s
        'AUTOTHROTTLE_ENABLED': True,  # 启动[自动限速]
        'AUTOTHROTTLE_DEBUG': True,  # 开启[自动限速]的debug
        # 'AUTOTHROTTLE_MAX_DELAY': 10,  # 设置最大下载延时
         'DOWNLOAD_TIMEOUT': 5,
        # 'CONCURRENT_REQUESTS_PER_DOMAIN': 32 # 限制对该网站的并发请求数
     }

    def parse(self, response, **kwargs):
        # r= requests.get(
        #     'https://ifconfig.me/ip')
        # print(r.text)

        # if not response.url:  # 接收到url==''时
        #     print('500')
        #     yield ZgzwItem(key=response.meta['key'], _str=500, alias='')
        # elif 'exception' in response.url:
        #     print('exception')
        #     yield ZgzwItem(key=response.meta['key'], _str='EXCEPTION', alias='')
        item= ZgzwItem()

        item['title']=str(response.xpath('//*[@id="box"]/tr[1]/td[2]/text()').get()).replace("\xa0","")
        item['a_number'] =str(response.xpath('//*[@id="box"]/tr[1]/td[4]/text()').get()).replace("\xa0","")
        item['a_day'] = str(response.xpath('//*[@id="box"]/tr[1]/td[4]/text()').get()).replace("\xa0","")
        item['p_number'] = str(response.xpath('//*[@id="box"]/tr[2]/td[2]/text()').get()).replace("\xa0","")
        item['p_day'] = str(response.xpath('//*[@id="box"]/tr[2]/td[4]/text()').get()).replace("\xa0","")
        item['applicant'] = str(response.xpath('//*[@id="box"]/tr[3]/td[2]/text()').get()).replace("\xa0","")
        item['address'] = str(response.xpath('//*[@id="box"]/tr[3]/td[4]/text()').get()).replace("\xa0","")
        item['inventor'] = str(response.xpath('//*[@id="box"]/tr[5]/td[2]/text()').get()).replace("\xa0","")
        item['code'] = str(response.xpath('//*[@id="box"]/tr[10]/td[2]/text()').get()).replace("\xa0","")
        item['abstract'] =str( response.xpath('//*[@id="box"]/tr[11]/td[2]/text()').get()).replace("\xa0","")
        item['principal'] = str(response.xpath('//*[@id="box"]/tr[12]/td[2]/text()').get()).replace("\xa0","")
        item['pages'] = str(response.xpath('//*[@id="box"]/tr[13]/td[2]/text()').get()).replace("\xa0","")
        item['m_number'] = str(response.xpath('//*[@id="box"]/tr[14]/td[2]/text()').get()).replace("\xa0","")
        item['c_number'] = str(response.xpath('//*[@id="box"]/tr[15]/td[2]/text()').get()).replace("\xa0","")
        item['agency'] = str(response.xpath('//*[@id="box"]/tr[8]/td[2]/text()').get()).replace("\xa0","")
        item['agent'] = str(response.xpath('//*[@id="box"]/tr[8]/td[4]/text()').get()).replace("\xa0","")
        yield item

        while(self.s<99999):

           self.s+=1
           self.offset=str(self.s).zfill(5)
           url='https://dbpub.cnki.net/grid2008/dbpub/detail.aspx?dbcode=SCPD&dbname=SCPD2020&filename=CN1046'+str(self.offset)+'A'
           yield scrapy.Request(url, callback=self.parse)

