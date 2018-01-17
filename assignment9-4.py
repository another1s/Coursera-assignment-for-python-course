lst=list()
fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "text.txt"
fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From '):
        words=line.strip()
        words=words.split()
        #print(words[1])
        count=count+1
        lst.append(words[1])
#print("There were", count, "lines in the file with From as the first word")
m=dict()
for keys in lst:
    m[keys]=m.get(keys,0)+1
#print(m.values())
maxinum=max(m.values())
if keys in m:
    if m[keys]==5:
        name=keys
print(name,maxinum)
#print(lst)


#D:\pythoncode\text.txt
