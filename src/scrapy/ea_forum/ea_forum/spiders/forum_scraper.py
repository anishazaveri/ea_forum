
import scrapy
import pandas as pd
link_file = pd.read_csv('../../../data/ea_forum/2020/links.csv')
links = link_file[link_file['Link'].str.contains(
    "https://forum.effectivealtruism.org/posts/")]['Link'].to_list()


class forum_scraper(scrapy.Spider):
    name = "forum_scraper"

    def start_requests(self):
        urls = links
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'date': response.xpath("//span[@class='PostsPageDate-date']/span/text()").get(),
            'title':
            response.xpath(
                "//h1[@class='MuiTypography-root MuiTypography-display3 PostsPageTitle-root']/text()").get(),
            'author': response.xpath("//span[@class='PostsAuthors-authorName']/span/span/a/text()").get(),
            'num_comments': response.xpath("//a[@class='PostsPage-commentsLink']/text()").get(),
            'num_karma': response.xpath("//h1[@class='MuiTypography-root MuiTypography-headline PostsVote-voteScore']/text()").get(),
            'content': response.xpath("//div[@class='PostsPage-postContent']").get(),
        }
