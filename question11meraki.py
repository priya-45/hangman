dict = {'a':50, 'b':58,'c':56,'d':40, 'e':100, 'f':20}
m=[]
for i in dict:
    m.append(dict[i])
# print(m)
i=0
max=0
l=[]
while i<len(m):
    if m[i]>max:
        max=m[i]
    i=i+1
j=0
nmax=0
while j<len(m):
    if m[j]>nmax:
        if m[j]<max:
            nmax=m[j]
    
    j=j+1
k=0
mmax=0
while k<len(m):
    if m[k]>mmax:
        if m[k]<nmax:
            mmax=m[k]
    k=k+1
l.append(nmax)
l.append(mmax)
l.append(max)
print(l)