# Cau6. Duong Van Quynh - DHKL18A1HN - 24174600058


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack): 
            print(item)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack contents (from top to bottom):")
    stack.print()
    print("Stack size:", stack.size())
    print("Pop top element:", stack.pop())
    print("Stack size after pop:", stack.size())
    print("Is stack empty?", stack.is_empty())