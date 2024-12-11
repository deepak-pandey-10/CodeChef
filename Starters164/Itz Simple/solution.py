t=int(input())
for i in range(t):
    n,k,p=map(int,input().split())
    a=list(map(int,input().split()))
    k+=max(a)
    a.remove(max(a))
    p+=sum(a)
    if k>p:
        print("Ved")
    elif k<p:
            print("Varun")
    else:
        print("Equal")