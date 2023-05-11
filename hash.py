from linkedList import LinkedList
def getNonRepeated(sentence:str):
    repeated =dict()
    for char in sentence:
        repeated[char]=repeated.get(char,0)+1
    return sorted(repeated.items(),key= lambda item:item[1])[0]

def getRepeated(sentence:str):
    repeated= set()
    for char in sentence:
        if char in repeated:
            return char
        repeated.add(char)

class Entry:
    def __init__(self,key,value):
        self.key=key
        self.value=value
    def __str__(self):
        return f"{self.key}:{self.value}"


class Hash:
    def __init__(self,size):
        self.entries = []
        for i in range(size):
            self.entries.append(LinkedList())   
        self.size = size

    def hash(self,key:int):
        return key% self.size
    
    def put(self,key:int,value):
        entry = self.get(key)
        if entry:
            entry.value = value
            return
        entry = Entry(key,value)
        hashkey = self.hash(key)
        self.entries[hashkey].add_last(entry)

    def remove(self,key:int):
        hashkey = self.hash(key) 
        packet = self.entries[hashkey]
        if packet.is_empty():
            KeyError("this key is not present")

        current = packet.first
        previous = current
        while current and current.data.key !=key:
            previous = current
            current = current.next
        if current is None:
            raise KeyError("this key is not present")
        if current == previous:
            packet.delete_first()
        else:
            previous.next = current.next


    def get(self,key:int)->Entry:
        hashkey = self.hash(key)
        packet = self.entries[hashkey]
        if packet.is_empty():return None

        current = packet.first
        while current and current.data.key != key:
            current = current.next
        return current.data if current else None




if __name__ == '__main__':
    hash = Hash(5)
    hash.put(32,'ikram')
    hash.put(23,'khan')
    hash.put(13,'qaseem')
    hash.put(21,"hamd")
    hash.remove(23)
    print(hash.get(13))
    hash.remove(21)
    hash.put(21,"kako")
    print(hash.get(21))

