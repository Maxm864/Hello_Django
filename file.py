
n1 = 4
n2 = 6
with open('inn.txt','w') as f:
    f.write(str(n2) + ' ' +  str(n1))
with open('ot.txt','w') as f_1:
    f_1.write(str(n1 - n2))
