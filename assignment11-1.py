import re

file_name=input("please input your file name:")
handle=open(file_name)

lst=list()
lst.append('123')
sum=0
num=0
for line in handle:
    line=line.strip()
    number=re.findall('[0-9]+',line)
   # print(number)
    if len(number)!=0 :
        count=0                                  #此处遍历每一行得到的是存有所有数字的list
        while count<len(number):
          num=num+int(number[count])
          count=count+1
    else :
        continue
print(num)
print(type(lst[0]))
sum
#D:\pythoncode\11-1\text.txt