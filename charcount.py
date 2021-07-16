x=input("enter the string")
d=dict()
for keys in x:
    d[keys]=d.get(keys,0)+1
print(d)
