import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
xml = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)
comments = tree.findall('comments/comment')
total=0
for comment in comments:
    total += int(comment.find('count').text)
print(total)