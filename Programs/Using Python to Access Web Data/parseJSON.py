import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location - ')
data = urllib.request.urlopen(url, context=ctx).read()
print("Retrieving", url)

info = json.loads(data)
print("Retrieved", len(data), "characters")
print("Count:", len(info['comments']))
total = 0
for item in info['comments']:
    total += item['count']
print("Sum:", total)
