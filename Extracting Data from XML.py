import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://py4e-data.dr-chuck.net/comments_30423.xml'
sum=0

   # name = input('Enter name: ')
   # if len(address) < 1: break
  #  url = serviceurl + urllib.parse.urlencode({'address': address})
url=serviceurl
#print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print(data)
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
print(results,len(results))
for elements in results:
    _name = elements.find('name').text
    _count = elements.find('count').text
    print(_name,_count)
    sum=sum+int(_count)
print('sum',sum)


#http://py4e-data.dr-chuck.net/comments_42.xml