dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
k={}
for x in dic1:
    for y in dic2:
        for z in dic3:
            if x==y:
                p=(dic1[x]+dic2[y])
            
k.update({1:10})
k.update({x:p})
k.update({3:30})
k.update({5:50})
k.update({6:60})
print(k)