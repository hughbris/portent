from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from port.items import PortVisit

class LpcSpider(BaseSpider):
	name = 'lpc.co.nz'
	allowed_domains = ['lpc.co.nz']
	start_urls = [
		'http://www.lpc.co.nz/RP.jasc?Page=/LPCShipsInPortNetApp',
	]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		headingTable = hxs.select("//table[tr/td[1][@class='searchBarHeading']]") #FWIW
		dataTable = hxs.select("//*[@class='tinyTable']/table")
		updateTime = dataTable.select("normalize-space(substring-after(../preceding-sibling::p/b/text(),':'))") #XXX hmm, there might be a more robust path for this ..
		columnHeadingRow = dataTable.select("tr[1]") #FWIW, again
		row = columnHeadingRow.select("following-sibling::tr")
		visits = []
		for r in row:
			if r.select("td[@class='h3']"): #this markup really exists
				vessel_category =  r.select("td/text()").extract()
			else:
				visit = PortVisit()
				visit['category'] = vessel_category
				(
					visit['vessel'], 
					visit['berth'], 
					visit['arrival'], 
					visit['origin'], 
					visit['departure'], 
					visit['destination'], 
					visit['agent'], 
					visit['cargo']
				) = r.select("td/text()").extract()
				visits.append(visit)
		return visits
