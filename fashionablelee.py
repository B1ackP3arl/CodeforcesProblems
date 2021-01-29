n=int(input().strip())
res=[]
for _ in range(n):
    temp=int(input())
    if temp%4 == 0:
        res.append("YES")
    else:
        res.append("NO") 
for items in res:
    print(items)    
