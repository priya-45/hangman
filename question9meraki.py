a="MISSISSIPPI"
d=list(a)
i=0
a={}
while i<len(d):
	count=0
	b={}
	j=0
	while j<len(d):
		if d[i]==d[j]:
			count+=1
		j=j+1
	a.update({d[i]:count})
	i+=1
print(a)


# i=0
# c,c1,c2,=0,0,0
# c3=0
# m={}
# while i<len(a):
#     if a[i]=='M':
#         c=c+1
#     if a[i]=="I":
#         c1=c1+1
#     if a[i]=="S":
#         c2=c2+1
#     if a[i]=="P":
#         c3=c3+1
#     i=i+1
# p=a[0]
# f=a[1]
# g=a[2]
# d=a[8]
# m.update({p:c})
# m.update({f:c1})
# m.update({g:c2})
# m.update({d:c3})
# print(m)