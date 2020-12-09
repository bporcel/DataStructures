# Creating an array.

class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]
    
    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return item
   
    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return lastItem

    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)
        del self.data[self.length-1]
        self.length -= 1
        return item

    def shiftItems(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i+1]

    def __str__(self):
        string = ''
        for i in range(self.length):
            if i == self.length -1:
                string += str(self.data[i])
            else:
                string += str(self.data[i])+', '

        return '[{}]'.format(string)

array = MyArray()

print(array.push('hello'))
print(array.push('world'))
print(array.push('!'))
print(array.get(0))
print(array.pop())
print(array.delete(1))
print(array)
