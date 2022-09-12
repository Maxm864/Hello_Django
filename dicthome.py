a = [12,13,14,15,16]
d = dict(zip(a,a))
print(d)

q = [12,13,14,15]
count =0
for i in q:
 for j in str(i):
  if int(j) == 1:
   count +=1
print(count)