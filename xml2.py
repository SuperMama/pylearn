import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url=input('Enter:')
uh=urllib.request.urlopen(url)
data = uh.read()
list=[]
sum = 0

tree = ET.fromstring(data)

lst=tree.findall('comments/comment')

for item in lst:
    list.append(item.find('count').text)

for s in list:
    sum=sum+int(s)

print(sum)
