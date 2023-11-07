class Stack:
    def __init__(self):
        self.list = []

    def push(self, obj):
        self.list.append(obj)

    def pop(self):
        if self.list == []:
            return None
        else:
            return self.list.pop(0)


    def pick(self):
        temp = None
        if self.list == []:
            return temp
        else:
            temp = self.list[0]
        return temp


stack = Stack()
stack.push(4)
stack.push(40)
stack.push("Eu sunt")
print(stack.list)
print(stack.pop())
print(stack.list)
a = stack.pick()
print(a)
print(stack.list)
stack2 = Stack()
print(stack2.pop())