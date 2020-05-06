
import scrapy
import pandas as pd
from pathlib import PureWindowsPath
link_file = pd.read_csv(PureWindowsPath(
    r"C:\Users\light\Dropbox (Personal)\Projects\ea_forum\data\ssc\links.csv"))
mask = ((link_file['Link'].str.contains(
    "https://slatestarcodex.com/")) & (link_file['Link'].str.len() > 35))

links = link_file[mask]['Link'].to_list()


class ssc_scraper(scrapy.Spider):
    name = "ssc_scraper"

    def start_requests(self):
        urls = links
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'date': response.xpath('//span[@class="entry-date"]/text()').get(),
            'title':
            response.xpath("//title/text()").get(),
            'author': response.xpath('//a[@class="url fn n"]/text()').get(),
            'num_comments': response.xpath('//h3[@id="comments-title"]/text()').get(),
            'content': response.xpath('//div[@class="pjgm-postcontent"]').get()
        }
