
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __iniy__(self):
        self.head = None
    def printlist(self):
        temp  = self.head
        while temp:
            print(temp.data)
            temp =temp.next

    # def push(self,new_element):
    #     new_node =Node(new_element)
    #     new_node.next = self.head
    #     self.head= new_node

    # def keyin(self,next1,new1_e):
    #     new2 =Node(new1_e)
    #     new2.next=next1.next
    #     next1.next=new2

    # def append(self,element):
    #     new_tup = Node(element)

    #     if self.head is None:
    #         self.head=new_tup
    #         return  
    #     last=self.head
    #     while last.next:
    #         last=last.next
    #     last.next=new_tup

    def deleteNode(self,key):
        temp1= self.head
        if (temp1  and temp1.data==key):
            self.head=temp1.next
            temp1=None
            return
        while temp1:
            if temp1.data==key:
                break
            oldingi= temp1
            temp1=temp1.next
        if temp1==None:
             return
        oldingi.next=temp1.next
        temp1=None
            


            

    
