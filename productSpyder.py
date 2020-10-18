import scrapy
from scrapy.shell import inspect_response
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ProductSpyder(CrawlSpider):
    name = "products"

    custom_settings = {
        "USER_AGENT": "cool_project",
    }

    rules = (
        Rule(LinkExtractor(allow=('/ip/',)), callback="parse_item"),
        Rule(LinkExtractor(allow=('/cp/',))),
        Rule(LinkExtractor(allow=('/browse/',))),
    )

    start_urls = [
        'https://www.walmart.com/cp/clothing/5438?povid=FashionGlobalNav_ShopAll'
        'https://www.walmart.com/cp/electronics/3944'
        'https://www.walmart.com/cp/home/4044?povid=4044+%7C+2019-08-30+%7C+ShopAllHomeGFlyout'
        'https://www.walmart.com/cp/baby-products/5427?povid=BabyGlobalNav_ShopAllBaby'
        'https://www.walmart.com/cp/toys/4171?&povid=4171+%7C+contentZone20+%7C+2016-11-08+%7C+1+%7C+Toys+Flyout'
        'https://www.walmart.com/cp/food/976759'
        'https://www.walmart.com/cp/pet-supplies/5440?povid=5440+%7C+2018-04-30+%7C+all%20pets%20dept%20flyout&povid=5440+%7C+2018-04-30+%7C+super%20dept%20flyout%20all%20pets'
        'https://www.walmart.com/cp/beauty/1085666?povid=BeautyGlobalNav_ShopAllBeauty'
        'https://www.walmart.com/cp/personal-care/1005862'
        'https://www.walmart.com/cp/arts-crafts-and-sewing/1334134'
        'https://walmart.com/all-departments'
    ]

    def parse_start_url(self, response):
        title = response.css("h1.prod-ProductTitle::text").get()
        price = response.css(".price-characteristic::attr(content)").get()
        avg_review = response.css(".ReviewsRating-rounded-overall").css(".font-bold::text").get()
        try:
            num_reviews = int(response.css('.ReviewRatingWYR-container').xpath("div/div[2]/text()").get().split()[0])
        except:
            num_reviews = 0
        desc_text = response.css(".about-desc.about-product-description.xs-margin-top *::text").get()
        desc_list = response.css(".about-desc.about-product-description.xs-margin-top li::text").getall()
        prod_category = response.css(".breadcrumb[data-automation-id=breadcrumb-item-0] span::text").get()
        """
        yield {
            "title": title,
            "price": price,
            "avg_review": avg_review,
            "num_reviews": num_reviews,
            "desc_text": desc_text,
            "desc_list": desc_list,
            "prod_category": prod_category,
        }
        """

    def parse_item(self, response):
        url = response.url
        title = response.css("h1.prod-ProductTitle::text").get()
        price = response.css(".price-characteristic::attr(content)").get()
        avg_review = response.css(".ReviewsRating-rounded-overall").css(".font-bold::text").get()
        try:
            num_reviews = int(response.css('.ReviewRatingWYR-container').xpath("div/div[2]/text()").get().split()[0])
        except:
            num_reviews = 0
        desc_text = response.css(".about-desc.about-product-description.xs-margin-top *::text").get()
        desc_list = response.css(".about-desc.about-product-description.xs-margin-top li::text").getall()
        prod_category = response.css(".breadcrumb[data-automation-id=breadcrumb-item-0] span::text").get()
#        links = response.css('a[href*="/ip/"]::attr(href)').getall()

#        inspect_response(response, self)

        yield {
            "title": title,
            "url": url,
            "price": price,
            "avg_review": avg_review,
            "num_reviews": num_reviews,
            "desc_text": desc_text,
            "desc_list": desc_list,
            "prod_category": prod_category,
        }
#        print(price, avg_review, num_reviews, desc_text, desc_list)
