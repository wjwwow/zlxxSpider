# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from twisted.internet import defer
from twisted.internet.error import TimeoutError, DNSLookupError, \
    ConnectionRefusedError, ConnectionDone, ConnectError, \
    ConnectionLost, TCPTimedOutError
from scrapy.http import HtmlResponse
from twisted.web.client import ResponseFailed
from scrapy.core.downloader.handlers.http11 import TunnelError
from scrapy import signals
from fake_useragent import UserAgent
import requests
import random




class ZgzwSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZgzwDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    from twisted.internet import defer
    from twisted.internet.error import TimeoutError, DNSLookupError, \
        ConnectionRefusedError, ConnectionDone, ConnectError, \
        ConnectionLost, TCPTimedOutError
    from scrapy.http import HtmlResponse
    from twisted.web.client import ResponseFailed
    from scrapy.core.downloader.handlers.http11 import TunnelError
    #抛出异常
class ProcessAllExceptionMiddleware(object):
    ALL_EXCEPTIONS = (defer.TimeoutError, TimeoutError, DNSLookupError,
                      ConnectionRefusedError, ConnectionDone, ConnectError,
                      ConnectionLost, TCPTimedOutError, ResponseFailed,
                      IOError, TunnelError)
    def process_response(self,request,response,spider):
        #捕获状态码为40x/50x的response
        if str(response.status).startswith('4') or str(response.status).startswith('5'):
            #随意封装，直接返回response，spider代码中根据url==''来处理response
            response = HtmlResponse(url='')
            return response
        #其他状态码不处理
        return response
    def process_exception(self,request,exception,spider):
        #捕获几乎所有的异常
        if isinstance(exception, self.ALL_EXCEPTIONS):
            #在日志中打印异常类型
            print('Got exception: %s' % (exception))
            #随意封装一个response，返回给spider
            response = HtmlResponse(url='exception')
            return response
        #打印出未捕获到的异常
        print('not contained exception: %s'%exception)

class RandomUserAgentMiddlware(object):
    '''随机更换user-agent，基本上都是固定格式和scrapy源码中useragetn.py中UserAgentMiddleware类中一致'''
    def __init__(self,crawler):
        super(RandomUserAgentMiddlware,self).__init__()
        self.ua= UserAgent()        #从配置文件settings中读取RANDOM_UA_TYPE值，默认为random，可以在settings中自定义
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE","random")

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)

    def process_request(self,request,spider):#必须和内置的一致，这里必须这样写
                def get_ua():
                    return getattr(self.ua,self.ua_type)
                request.headers.setdefault('User-Agent',get_ua())
                print( request.headers.setdefault('User-Agent',get_ua()))


# class ProxyMiddleWare(object):
#     """docstring for ProxyMiddleWare"""
#
#     def get_proxy(self):
#
#         return requests.get("http://127.0.0.1:5010/get/").json()
#
#     def delete_proxy(proxy):
#         requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
#
#     def process_request(self,request, spider):
#
#         '''对request对象加上proxy'''
#         proxy = self.get_proxy().get("proxy")
#         print("this is request ip:"+proxy)
#         request.meta['proxy'] = 'http://'+proxy
#         # request.meta['proxy'] = 'http://123.139.56.238:9999'
#         print(request.meta['proxy'])


    # def process_response(self, request, response, spider):
    #     '''对返回的response处理'''
    #     # 如果返回的response状态不是200，重新生成当前request对象
    #     if response.status != 200:
    #         print('删除代理' + self.proxy)
    #         requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(self.proxy))
    #         proxy = self.get_random_proxy()
    #         print("获得新代理" + proxy)
    #         # 对当前reque加上代理
    #         request.meta['proxy'] = proxy
    #         return request
    #     return response


