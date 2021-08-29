# factorialni rekursiya orqalli hisobash
def factl(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factl(n-1)
t=factl(5)
print(t)