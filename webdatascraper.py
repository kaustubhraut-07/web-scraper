import scrapy
import os


# the structure and naming conventions are necessary as scrapy will automalty call the urls that we write in the start_urls
# and after thet it will pass the flow to the parse function and alos it is necessry to write the function name as parse only

class FormSpider(scrapy.Spider):
    name = "form_spider"
    start_urls = [
        "https://blog.bytebytego.com/p/ep104-how-do-search-engines-work",
        "https://www.wikipedia.org/",
        "https://www.flipkart.com/"
    ]

    def parse(self, response):
        if response.status == 200:
            full_html = response.text
            self.logger.info(f"Fetched content with length: {len(full_html)}")

            # Creating unique file naem 
            url_parts = response.url.split('//')
            domain = url_parts[1].split('/')[0]
            filename = f"{domain.replace('.', '_')}.html"

            try:
                with open(filename, "w", encoding='utf-8') as f:
                    f.write(full_html)
                self.logger.info(f"Content written to {filename}")
            except Exception as e:
                self.logger.error(f"Failed to write content to {filename}: {e}")
        else:
            self.logger.error(f"Failed to fetch content. Status code: {response.status}")

        return None
