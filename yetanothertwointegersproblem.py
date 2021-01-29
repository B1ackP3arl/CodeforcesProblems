def steps(a,b):
    gap=a-b
    res=gap//10
    reminder=gap%10
    if reminder==0:
        return res
    else:
        return res+1    



if __name__=="__main__":
    n=int(input())
    li=[]
    for _ in range(n):
        a,b=map(int,input().split())
        if (a>b):
            s=steps(a,b)
            li.append(s)
        elif(a==b):
            li.append(0)
        else:
            s=steps(b,a)
            li.append(s)

for items in li:
    print(items)
        