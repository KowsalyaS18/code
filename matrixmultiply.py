m1=[[1,2,3],
    [4,6,2],
    [3,6,7]]

m2=[[2,8,9],
    [3,4,5],
    [6,7,9]]
    
result=[[0,0,0],
     [0,0,0],
     [0,0,0]]
     
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            result[i][j]+=m1[i][k]*m2[k][j]

for r in result:
    print(r)

