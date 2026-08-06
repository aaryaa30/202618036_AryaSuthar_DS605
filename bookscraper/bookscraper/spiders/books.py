import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com/"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    custom_settings = {
        "LOG_LEVEL": "ERROR"
    }

    def parse(self, response):

    
        for book in response.css("article.product_pod h3 a::attr(href)").getall():
            yield response.follow(book, callback=self.parse_book)

        
        current = int(response.url.split("page-")[1].split(".")[0])

        
        if current < 5:
            next_page = f"https://books.toscrape.com/catalogue/page-{current + 1}.html"
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_book(self, response):

        rating = response.css("p.star-rating::attr(class)").get(default="")
        rating = rating.replace("star-rating ", "")

        description = response.css("#product_description + p::text").get()
        if description is None:
            description = "No description"

        availability = " ".join(
            text.strip()
            for text in response.css("p.availability::text").getall()
            if text.strip()
        )

        yield {
            "Title": response.css("h1::text").get(),
            "Category": response.css("ul.breadcrumb li:nth-child(3) a::text").get(),
            "Price": response.css("p.price_color::text").get(),
            "Rating": rating,
            "Availability": availability,
            "Description": description,
            "UPC": response.xpath('//th[text()="UPC"]/following-sibling::td/text()').get(),
            "Number of Reviews": response.xpath('//th[text()="Number of reviews"]/following-sibling::td/text()').get(),
            "Product URL": response.url,
        }