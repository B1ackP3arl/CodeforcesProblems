if __name__ == "__main__":
    t = int(input())
    arr = [2020 , 2021]
    c = 0
    # t = 1
    for _ in range(t):
        n = int(input())
        d  = n // arr[0]
        r = n % arr[0]
        tsm = r * arr[1]
        if tsm == n :
            print("YES")
        elif tsm < n :
            while tsm < n :
                tsm += arr[0]  
                if tsm == n :
                    print("YES") 
                    c += 1
                    break
            if c == 0 :
                print("NO")
        else:
            print("NO")        