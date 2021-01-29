from collections import Counter
t  = int(input())
# t = 1
for _ in range(t):
    n = int(input())
    # arr = [1,1,1,1,1]

    arr  = list(map(int,input().split()))
    res = list(Counter(arr).items())
    res1 = res.sort()
    # print(res)
    if len(res) == 2 :
        temp = res[1][1] % 2
        # print(temp)
        if temp != 0:
            temp1 = res[0][1] - temp*2
            print('YES') if temp1%2 == 0 else print('NO')
        else:
            print('YES') if res[0][1] %2 == 0 else print('NO')

    else:
        print('YES') if len(arr)%2 == 0 else print('NO')


 
    
