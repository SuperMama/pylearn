import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
input = '''
<stuff>
    <users>
        <user x='2'>
            <id>001</id>
            <name>Pritam</name>
        </user>
        <user x='7'>
            <id>007</id>
            <name>Starc</name>
        </user>
    </users>
</stuff>'''

stuff=ET.fromstring(input)
lst=stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name:',item.find('name').text)
    print('ID:',item.find('id').text)
    
