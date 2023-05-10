
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return self.stack == []
    
def reverseString(str:str):
    stack = Stack()
    for char in str:
        stack.push(char)
    reversed=""
    while not stack.isEmpty():
        reversed += stack.pop()
    return reversed

brackets = {
        ">":"<",
        ")":"(",
        "]":"[",
        "}":"{",
        }

def balancedString(str:str):
    stack = Stack()
    for char in str:
        if char in brackets.values():
            stack.push(char)
        elif char in brackets.keys():
            if stack.isEmpty():
                return False
            if not brackets[char] is stack.pop():
                return False             
    return stack.isEmpty()


if __name__ == "__main__":
    print(balancedString("(1+2))"))

