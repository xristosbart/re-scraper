import scrapy

class HomeSalesSpider(scrapy.Spider):
    name = 'homesales'
    allowed_domains = ['rightmove.co.uk']
    start_urls = ['https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E87490&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false']

    def parse(self, response):
        yield from response.follow_all(css='.l-searchResult a.propertyCard-link', callback=self.parse_listing)
        #TODO: infinite scroll

    def parse_listing(self, response):
        print(response.css('#root > main > div > div.WJG_W7faYk84nW-6sCBVi > div > article._2fFy6nQs_hX4a6WEDR-B-6 > div > div > div._1gfnqJ3Vtd1z40MlC0MzXu > span:nth-child(1)::text').get())
    
        # url = response.url
        # downlink = response.urljoin(response.xpath('//*[@id="light"]/div/p[3]/a[1]/@href').get())
        # tags = response.xpath('//*[@id="info"]/p[7]/a/text()').getall()
        # item=Design(url=url, downlink=downlink, tags=tags, status='Unknown')
        # yield item