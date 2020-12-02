class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, value: str) -> None:
        self.data.append(value)

    def pop(self) -> str:
        if len(self.data) > 0:
            removedElement = self.data[0]
            del self.data[0]
            return removedElement

    def peek(self) -> str:
        if len(self.data) > 0:
            return self.data[0]

    def empty(self) -> bool:
        return True if len(self.data) == 0 else False

    def __str__(self):
        return str(self.data)


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push('Google')
obj.push('Github')
obj.push('StackOverflow')
print(obj)
param_2 = obj.pop()
print('Removed element ->', param_2)
print(obj)
param_3 = obj.peek()
print('Peek ->', param_3)
param_4 = obj.empty()
print('Is Empty ->', param_4)
param_2 = obj.pop()
param_2 = obj.pop()
print(obj)
param_4 = obj.empty()
print('Is Empty ->', param_4)
