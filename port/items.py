# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PortVisit(Item):
    category = Field()
    vessel = Field()
    berth = Field()
    arrival = Field()
    origin = Field()
    departure = Field()
    destination = Field()
    agent = Field()
    cargo = Field()
