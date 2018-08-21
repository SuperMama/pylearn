import re
#datafile=input("Enter file name:")
#if len(datafile)<1:
datafile='Actual Data.txt'
fileop=open(datafile)
'''nos=list()
sum=0
for line in fileop:
    line.strip()
    y=re.findall('([0-9]+)',line)
    for x in y:
        nos.append(x)
print(nos)
for n in nos:
    sum=sum+int(n)
print(sum)

a=[1,2,3]
sum+int(a) for x in a


print(sum(sum=) )'''
#sum=0
#print(sum+int(x) for x in [x for line in fileop for x in re.findall('([0-9]+)',line.strip())])
a=[1,2,3]
print(sum+x for x in a)
