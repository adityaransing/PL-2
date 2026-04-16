class Stack:
    def __init__(self):
        self.stack=[ ]
    def push(self,item):
        self.stack.append(item)
        print(f"{item}pushed into stack")
    def safe_pop(self):
        if len(self.stack)==0:
            print("Stack is empty,nothing to pop")
            return None
        else:
            return self.stack.pop()
    def display(self):
        print("Stack:", self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Popped element:",s.safe_pop())
print("Popped element:",s.safe_pop())
print("Popped element:",s.safe_pop())
print("Popped element:",s.safe_pop())
