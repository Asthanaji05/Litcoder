"""
Simple Text Editor
"""
class CustomStack:
    def __init__(self):
        self.data = ""
        self.history = []
        
    def insert(self, item):
        self.history.append(f"Insert {len(item)}")
        self.data += item
    
    def delete(self, n):
        items = self.data[:-n:-1]
        self.data = self.data[:len(self.data) - n]
        self.history.append(f"Delete {items}")
    
    def get(self, index):
        return self.data[index-1]
    
    def undo(self):
        last_operation = self.history[-1].split()
        
        if last_operation[0] == "Insert":
            self.data = self.data[:-last_operation[1]]
        if last_operation[0] == "Delete":
            self.data += last_operation[1]
        self.history.pop()
        
custom_stack = CustomStack()
inputVal = list(map(lambda x: x.split(), input().split(",")))
for op, val in inputVal:
    if op == '1':
        custom_stack.insert(val)
    elif op == '2':
        custom_stack.delete(int(val))
    elif op == '3':
        print(custom_stack.get(int(val)))
                                                                                                                            