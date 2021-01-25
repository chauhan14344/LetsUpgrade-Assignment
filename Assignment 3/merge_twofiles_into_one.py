# Python program to merge two files into a third file
content1 = content2 = ""  
with open('D:\\filea.txt') as fp: 
    content1 = fp.read() 

with open('D:\\fileb.txt') as fp: 
    content2 = fp.read() 
content1 += "\n"
content1 += content2 
  
with open ('D:\\filec.txt', 'w') as fp: 
    fp.write(content1) 





