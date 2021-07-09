myList1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
a = int(input())
def linar(list1,n):
    for i in range(len(list1)):
        if list1[i]==n:
            return i
    return "None"
print(linar(myList1,a))
    




