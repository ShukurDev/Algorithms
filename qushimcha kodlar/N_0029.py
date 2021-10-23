n=int(input())
a=[]
k=0
for i in range(1,n+1):
    q=int(input())
    a.append(q)
for i in a:
    for j in range(1,i+1):
        if i%j==0:
            if j%2==0:
                k+=1
            else:
                continue
        else:
            continue
    print(k)
    k = 0
