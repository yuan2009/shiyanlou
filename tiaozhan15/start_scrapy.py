#!/usr/bin/env python3
import scrapy

class shiyanlou_scrapy_spider(scrapy.Spider):
    name = 'shiyanlou'
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self, response):
        for data in response.css('li.public'):
            yield {
                'name': data.css('div.mb-1 a::text').re_first('\n +([a-zA-Z-]+)*'),
                'update_time': data.css('div.mt-2 relative-time::attr(datetime)').extract_first()
            }
