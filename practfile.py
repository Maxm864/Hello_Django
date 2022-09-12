f = open('file.txt','r')
c = 0
for i in f:
    c+=1
    print('Кол-во символом в строке',len(i.strip()))
print('Кол-во строк',c)








