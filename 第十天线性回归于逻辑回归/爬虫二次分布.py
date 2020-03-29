import requests
from lxml import etree
url = 'http://www.360doc.com/content/17/1231/22/9200790_718001949.shtml'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
data= requests.get(url=url,headers=headers).text

tree = etree.HTML(data)
hua = tree.xpath('//span[@style="font-weight: 600;"]/text()')
print(hua)