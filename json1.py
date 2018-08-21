import urllib.request, urllib.parse, urllib.error
import json

url=input('Enter:')
uh=urllib.request.urlopen(url)
data = uh.read()
list=[]
sum = 0

info = json.loads(data)
list=[info]

for item in list:
    k=item['comments']
    for i in k:
        sum=sum+int(i['count'])
    #print('Id', item['id'])
    #print('Attribute', item['x'])
print(sum)
