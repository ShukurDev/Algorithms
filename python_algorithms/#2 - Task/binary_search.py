
list2=[1,3,4,6,7,8,10,12,23,45,56,78,99]
a = int(input())
def binary_s(list1,a):
    l=0
    a=int(a)
    h=int(len(list1)-1)
    if l>h:
        return "None"
    else:
        while True:
            m = (l+h)//2
            T = list1[m]
            T =int(T)
            if T == a:
                return m
           
            elif (T < a):
                if l==len(list1) or h!=len(list1):
                 break
                else:
                 l = m+1
                 continue
            elif T > a:
                if m==0 or l!=0:
                 break
                else:
                 h =m-1
                 continue
            else:
                break
    return "None"
print(binary_s(list2,a))