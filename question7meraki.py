u=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
p=[]
for i in range(len(u)):
    for j in u[i]:
        p.append(u[i][j])
print(p)
o=[]
i=0
while i<len(p):
    if p[i] not in o:
        o.append(p[i])
    i=i+1
print(o)