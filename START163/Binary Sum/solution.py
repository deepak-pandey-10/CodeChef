t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if n%2==1:
        if (n//2+1==k):
            print("YES")
        elif (n//2==k):
            print("YES")
        else:
            print("NO")
    else:
        if n//2==k:
            print("YES")
        else:
            print("NO")
