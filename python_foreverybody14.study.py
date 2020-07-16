from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter : ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    x = re.findall('[0-9]+',str(tag))
    for i in x:
        i = int(i)
        sum = sum + i

print(sum)