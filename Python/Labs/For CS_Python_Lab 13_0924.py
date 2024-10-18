"""
Queue using 2 stacks
"""
class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, item):
        self.data.append(item)
    
    def dequeue(self):
        temp = self.data[::-1]
        item = temp.pop()
        self.data = temp[::-1]
        return item
    
    def print(self):
        print(self.data[0])
    
inputVal = list(input().split(","))
queue = Queue()
for command in inputVal:
    if command[0] == "1":
        queue.enqueue(command[2:])
    elif command[0] == "2":
        queue.dequeue()
    elif command[0] == "3":
        queue.print()
                                                                                                                            