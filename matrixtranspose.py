m=[[2,5],
   [4,2],
   [6,8]]

ans=[[0,0,0],
     [0,0,0]]
     
for i in range(len(m)):
    for j in range(len(m[0])):
        ans[j][i]=m[i][j]
for a in ans:
    print(a)
