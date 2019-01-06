# -*- coding: utf-8 -*-
import scrapy

class Ringzer0flagSpider(scrapy.Spider):
    name = 'ringzer0flag'
    allowed_domains = ['ringzer0ctf.com']
    start_urls = ['https://ringzer0ctf.com/']

    def parse(self, response):
        #Extracting the username
        username = response.xpath("/html/body/div[2]/div/div[2]/div/table/tbody/node()/node()/a/text()").extract()

        #Extract the flags
        #flags = response.css(".score_flag::attr(src)").extract()

        #Extraxtint the points
        points = response.css(".points::text").extract()

        #Extracting gold
        gold = response.css('.gold::text').extract()

        #Extracting user info
        urls = response.xpath('/html/body/div[2]/div/div[2]/div/table/tbody/node()/node()/a/@href').extract()

        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

        #Give the extracted content row wise
        for item in zip(username, points, gold):
            #create a dictionary to store the scraped info
            scraped_info = {
                'username' : item[0],
                'points' : item[1],
                'gold': item[2]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info

        #follow pagination link
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        
        if next_page_url is not None:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):
        #Extracting username, country and member_since
        yield {
            'username': response.css('td.user_td_right::text')[0].extract(),
            'country': response.css('td.user_td_right::text')[1].extract(),
            'member_since': response.css('td.user_td_right::text')[2].extract()
        }
