import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        contents = response.xpath("//table[@id='example2']/tbody/tr")
        for content in contents:
            number = content.xpath('.//td[1]/text()').get()
            country_name = content.xpath('.//td[2]/a/text()').get()
            population = content.xpath('.//td[3]/text()').get()
            yearly_change = content.xpath('.//td[4]/text()').get()
            net_change = content.xpath('.//td[5]/text()').get()
            density = content.xpath('.//td[6]/text()').get()
            land_area = content.xpath('.//td[7]/text()').get()
            migrants = content.xpath('.//td[8]/text()').get()
            fert_rate = content.xpath('.//td[9]/text()').get()
            med_age = content.xpath('.//td[10]/text()').get()
            urban_pop = content.xpath('.//td[11]/text()').get()
            whole_share = content.xpath('.//td[12]/text()').get()

            yield {
                'no': number,
                'country': country_name,
                'population': population,
                'yearly_change': yearly_change,
                'net_change': net_change,
                'density': density,
                'land_area': land_area,
                'migrants': migrants,
                'fert_rate': fert_rate,
                'med_age': med_age,
                'urban_pop': urban_pop,
                'whole_share': whole_share
            }