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
#        Rule(LinkExtractor(allow=('/browse/',))),
    )

    start_urls = [
#        'https://www.walmart.com/ip/Rawlings-12-5-RGB36-Recreational-Baseball-Softball-Glove-Right-Hand-Throw/140817752'
#        'https://www.walmart.com/ip/Super-Smash-Bros-Ultimate-Special-Edition-Nintendo/162583898'
#        'https://www.walmart.com/ip/Cottonelle-Ultra-CleanCare-Strong-Toilet-Paper-12-Mega-Rolls-Bath-Tissue/331701566?wpa_bd=&wpa_pg_seller_id=F55CDC31AB754BB68FE0B39041159D63&wpa_ref_id=wpaqs:_zkFh0GbX72MldkEenFxk5IufInphxAfGMzSrL_aCMybOMUedwKb2Pd3XgJcLhgAgQSJ6odAn4kKNkJmVifRIMyecEfSqX7E-F74dv7PQG_F1TqFCGD93kzK4vvg3b_gS3KJ99kuOoWiPmv0bPOmqYvHZh49emuOcd_-M9izB9ceCn3cBBgM8HwHbj2xjx9dzvutgEcxFvKSYet36H1sSQ&wpa_tag=__tag__&wpa_aux_info=__aux_info__&wpa_pos=1&wpa_plmt=__plmt__&wpa_aduid=__aduid__'
#        'https://www.walmart.com/browse/electronics/2-in-1-laptops/3944_3951_1089430_1230091_1155872?page=2'
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
