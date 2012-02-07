# Scrapy settings for port project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'port'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['port.spiders']
NEWSPIDER_MODULE = 'port.spiders'
USER_AGENT = 'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0' #'%s/%s' % (BOT_NAME, BOT_VERSION)

