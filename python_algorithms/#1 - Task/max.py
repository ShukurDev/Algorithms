a,b,c = map(int,input().split())
if a>b:
    if a>c:
        print(f"{a} eng katta son.")
    else:
        print(f"{c} eng katta son.")
elif a<b:
    if b>c:
        print(f"{b} eng katta son.")
    else:
        print(f"{c} eng katta son.")
else:
    print(f"{c} eng katta son.")