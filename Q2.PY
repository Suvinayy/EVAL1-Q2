sentence="TCS is the largest IT Service company in India headquartered in Mumbai and also the largest employee base"
words=sentence.split()
wordcount=len(words)
dictw={}
dictl={}
for x in words :
    for y in x:
        dictl[y]=0
for x in words :
    for y in x:
        dictl[y]+=1
print (dictl)
for y in words :
    dictw[y]=0
for z in words :
    dictw[z]+=1
print (dictw)