class Hashtable:
    def __init__(self):
        self.data = []

    def __str__(self):
        string = ''
        for d in self.data:
            string += str(d)+', '
        return '{}'.format(string)

    def add(self, key, value):
        address = self._hash(key)

        tmp = []
        tmp.append(key)
        tmp.append(value)
        if not self.data[address]:
            self.data[address] = tmp
        else:
            if not type(self.data[address][0]) == list:
                aux = self.data[address]
                self.data[address] = []
                self.data[address].append(aux)

            self.data[address].append(tmp)

    def get(self, key):
        address = self._hash(key)
        if self.data[address]:
            return self.data[address]
        return False

    def keys(self):
        keysList = []
        for d in self.data:
            if d is not None:
                if type(d[0]) == list:
                    for i in d:
                        if i[0] not in keysList:
                            keysList.append(i[0])
                else: 
                    keysList.append(d[0])

        return keysList

    def _hash(self, key):
        address = 0
        for i in str(key):
            address += ord(i)

        self._expandData(address)

        return address

    def _expandData(self, address):
        tmp = [None] * (address + 1)
        if len(tmp) > len(self.data):
            self.data.extend(tmp)


table = Hashtable()
table.add('name', 'Natalia')
print(table.get('name'))
table.add('name', 'Patata')
print(table.get('name'))
table.add(1, 'One')
print(table.get(1))
table.add(5, 'Five')
print(table.get(5))
print(table.keys())
# print(table)
