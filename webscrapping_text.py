from lxml import html;
import requests;
page = requests.get(http://store.steampowered.com/stats/);
tree = html.fromstring(page.content);
totalUsers = tree.xpath('//div[@class="statsTop"]/text()')
#This will create a list of prices
print(totalUsers);

#from lxml import html;
#import requests;
#page = requests.get(https://trends24.in/);
#tree = html.fromstring(page.content);
#totalUsers = tree.xpath('//div[@class="trend-card"]/text()')
##This will create a list of prices
#print(totalUsers);
