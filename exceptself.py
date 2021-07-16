list=[1,2,3,4,5]  
arr=[0]*len(list)  
for i in range(len(list)):  
    product=1  
    for j in range(len(list)):
        if(i==j):
            continue
        else:
            product*=list[j]  
        arr[i]=product  
print(arr)
