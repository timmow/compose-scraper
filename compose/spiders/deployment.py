# -*- coding: utf-8 -*-
import scrapy


class DeploymentSpider(scrapy.Spider):
    name = 'deployment'
    allowed_domains = ['localhost:8001']
    start_urls = ['http://localhost:8001/compose.html']

    def parse(self, response):
        table= response.css('table.box-table')
        rows = table.css('tr')
        for row in rows:
            for progress in row.css('.progress-bar-wrapper').extract():
                yield {'progress': progress}
