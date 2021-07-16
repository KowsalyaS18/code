heads=int(input("number of heads"))
legs=int(input("number of legs"))
rabbit=int(0)
chicken=int(0)
if(legs%2!=0):
    print("")
for i in range(heads+1):
    j=heads-i
    if(2*i)+(4*j)==legs:
        print("no of chicken=",i)
        print("no of rabbit=",j)
