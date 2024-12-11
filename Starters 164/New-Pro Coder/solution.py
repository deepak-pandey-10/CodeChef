n,m =map(int,input().split())
if n%2==1:
    if n//2>=m:
        print("PRO")
    else:
        print("NEWBIE")
else:
    if n//2>m:
        print("PRO")
    else:
        print("NEWBIE")