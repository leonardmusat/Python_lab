class Queue:
    def __init__(self):
        self.list = []

    def push(self, obj):
        self.list.append(obj)

    def pop(self):
        if self.list == []:
            return None
        else:
            return self.list.pop()


    def pick(self):
        temp = None
        if self.list == []:
            return temp
        else:
            temp = self.list[-1]
        return temp


queue = Queue()
queue.push(4)
queue.push(40)
queue.push("Eu sunt")
print(queue.list)
print(queue.pop())
print(queue.list)
a = queue.pick()
print(a)
print(queue.list)
queue2 = Queue()
print(queue2.pop())