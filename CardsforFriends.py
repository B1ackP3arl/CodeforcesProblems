def ghapan(a):
    cont = 1
    while(a%2 == 0):
        a = a/2 
        cont = cont*2
    # print(cont)
    return cont    
        

def counting(w,h,n):
    w_numb = ghapan(w)
    h_numb = ghapan(h)
    sm = w_numb *  h_numb
    # print(sm)
    if  sm >= n:
        return "YES"
    else:
        return "NO"
    
if __name__ == "__main__":
    t = int(input())
    # t = 1
    for _ in range(t):
        w,h,n = map(int,input().split())
        print(counting(w,h,n))