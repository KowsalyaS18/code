m1=[[1,2,3],
    [4,6,2],
    [3,6,7]]

m2=[[2,8,9],
    [3,4,5],
    [6,7,9]]
    
sum=[[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        sum[i][j]=m1[i][j]+m2[i][j]
        
for num in sum:
    print(num)
