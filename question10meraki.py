dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
for i in dict1:
    # c=0
    # c=c+len(dict1[i])
    f=dict1["Alex"]+dict1["David"]
p=len(f)
print("total count:",p)