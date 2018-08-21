import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ("Enter:")
html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html,'html.parser')
list=[]
sum=0

#Retrieve all of the anchor tags
tags=soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    list.append(tag.contents[0])
#print(list)
for s in list:
    sum=sum+int(s)
print(sum)
