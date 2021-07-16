list=['abcdefr','abcjiyk']
if not list:
    print(" ")
elif len(list)==1:
    print(list[0])
else:
    list.sort()
    ans=" "
    for i in range(len(list[0])):
        if list[0][i]==list[-1][i]:
            ans+=list[0][i]
        else:
            break
        
    print(ans)  
