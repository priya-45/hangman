a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
p=list(a.values())
p.sort()
q=p.copy()
q.reverse()
s={}
for i in p:
    for j in a:
        if i==a[j]:
            s[j]=i
            print(q)
print(s)
o={}
for j in q:
    for k in a:
        if j==a[k]: 
            o[k]=j
print(o)


# m=[]
# k={}
# for i in a:
#     g=a[i]
#     m.append(g)
#     m.sort()
#     k={a[i]:m(str[i])}
# print(k)        

# l=[]
# b={}
# for i in a:
#     l.append(a[i])
# print(l)
# max=0
# for j in a:
#     if a[j]>max:
#         max=a[j]
# print(max)
# j=1
# k=[]
# while j<=max:
#     if j in l:
#         k.append(j)
#     j=j+1
# print(k)