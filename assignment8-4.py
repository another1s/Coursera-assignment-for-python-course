word=list()
def str(words):
    count=0
    while count<len(words):
        if words[count] not in word :
            word.append(words[count])
            count=count+1
        else:
            count=count+1
            continue

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words=line.strip()
    words=words.split()
    str(words)
word.sort()
print(word)


#c:\python\text.txt