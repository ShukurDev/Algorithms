
from listlin import Node,linkedlist

list1 = linkedlist()

list1.head = Node("I get up earle.")

second = Node("I was breakfast at 6. ")

third = Node("I am doing homework now.")

list1.head.next= second
second.next = third
# print(list1.head.data,"\n")
# print(list1.head.next.data,"\n")
# print(list1.head.next.next.data,"\n")

# list1.push("I am gooing to have lunch at 12.")

# list1.printlist()

# list1.keyin(list1.head.next.next.next,"I will evening.")

# list1.append("Today!!!\n")

# list1.deleteNode("I get up earle")


list1.printlist()