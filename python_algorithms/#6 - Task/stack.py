# Yangi element ro’yxat boshiga qo’shiladi (push)
# Elementlarning indeksi (tartib raqami) bo’lmaydi
# Ma’lumotlar ro’yxat boshidan boshlab tartib bilan o’qiladi

class Stack:
    def __init__(self):
        self.stack=[]
    def Empty(self):
        return len(self.stack)==0
    def Push(self,st):
        self.stack.append(st)
    def Pop(self,data):
        if self.isEmpty():
            return "Bu stack bush"
        else:
            self.stack.pop(data)
    def Peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]
stack1=Stack()
check1=stack1.Empty()
print(check1)
check2=stack1.Push("Shukurali")
check2=stack1.Push("Sarvar")
check2=stack1.Push("Komila")
check2=stack1.Push("Shahlo")

print(stack1.stack)

