n=int(input())
arr = list(map(int,input().split()))
x=arr.copy()
arr.sort()
if x==arr:
    print("YES")
else:
    print("NO")

