#!/usr/bin/env python3
# -*- coding:utf8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
import os, re
import urllib.request

class XiaohuarSpider(scrapy.spiders.Spider):
    name = "xiaohuar"
    allowed_domains = ["xiaohuar.com"]
    start_urls = [
        "http://www.xiaohuar.com/hua"
    ]

    def parse(self, response):
        hxs = Selector(response)
        for url in self.__get_all_urls(hxs):
            yield Request(url,callback=self.parse)

        current_url = response.url
        if self.__is_valid_item_url(current_url):
            items = hxs.xpath('//div[@class="item_list infinite_scroll"]/div')
            for i in range(len(items)):
                self.__retrieve_item(hxs,i)
                
        # body = response.body
        # unicode_body = response.body_as_unicode()

    def __get_all_urls(self, hxs):
        all_matched_urls = []
        all_urls = hxs.xpath('//a/@href').extract()
        for url in all_urls:
            if url.startswith('http://www.xiaohuar.com/list-1-'):
                all_matched_urls.append(url)
        
        return all_matched_urls

    def __is_valid_item_url(self,url):
        return re.match('http://www.xiaohuar.com/list-1-\d+.html', url)

    def __retrieve_item(self, hxs, index):
        src = hxs.xpath('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src' % index).extract()
        name = hxs.xpath('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % index).extract()
        school = hxs.xpath('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % index).extract()

        if src:
            ab_src = 'http://www.xiaohuar.com'+src[0]
            file_name = "%s_%s.jpg" % (school[0],name[0])
            file_path = os.path.join(os.getcwd(),'images',file_name)
            print("download src=%s, filename=%s" % (ab_src,file_path))
            self.__save(ab_src,file_path)
            
            
            #urllib.request.urlretrieve(ab_src,file_path)

    def __save(self, src, filepath):
        download_req = urllib.request.Request(
                    src,
                    headers={
                        'Host': 'www.xiaohuar.com',
                        'User-Agent' : ' Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
                        'Accept' : ' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language' : ' zh-CN,en-US;q=0.7,en;q=0.3',
                        'Accept-Encoding' : ' gzip, deflate',
                        'Referer' : ' http://www.xiaohuar.com/hua',
                        'Connection' : ' keep-alive'
                        #'Cookie' : ' __cfduid=dcbc267852b6cdb5f7d2d1d9c32c64e0e1489821563; a2513_pages=9; a2513_times=1; Hm_lvt_0dfa94cc970f5368ddbe743609970944=1489821566; Hm_lpvt_0dfa94cc970f5368ddbe743609970944=1489821566; bdshare_firstime=1489821665130',
                    }
                )
        download_resp = urllib.request.urlopen(download_req)
        with open(filepath, 'wb') as img:
            img.write(download_resp.read())