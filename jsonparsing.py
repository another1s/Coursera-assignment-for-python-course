import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import json

url='http://py4e-data.dr-chuck.net/comments_30424.json'
data=urllib.request.urlopen(url)
data=data.read()
print(data)
_json=data.decode()
print(_json)

info = json.loads(_json)
print('User count:', len(info))
sum=0

for elements in info['comments']:
   sum=sum+int(elements['count'])
print(sum)