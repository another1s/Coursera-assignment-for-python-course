file_name=input("input your file name:")
handle=open(file_name)

final=list()
for line in handle:
    if line.startswith('From '):
        lines=line.strip()                 #  此时lines为字符串
        words=lines.split()                 #split 操作后得到的一个list
        final.append(words[5])
d=dict()
for elements in final:
    elements=elements.split(':')            #split 操作后得到的一个list
    d[elements[0]]=d.get(elements[0],0)+1

for x,y in sorted(d.items()):
    print(x,y)

#D:\pythoncode\text.txt