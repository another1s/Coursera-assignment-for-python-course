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
        print(words[1])
        count=count+1
        if words[1] not in lst:
            lst.append(words[1])

#print(lst)
print("There were", count, "lines in the file with From as the first word")

#D:\pythoncode\text.txt
