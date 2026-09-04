class DynamicArray:
    
    def __init__(self, capacity: int):
        self.dynamicArray = [None]*capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.dynamicArray[i]

    def set(self, i: int, n: int) -> None:
        self.dynamicArray[i] = n

    def pushback(self, n: int) -> None:
        if (self.size == self.capacity):
            self.resize()
        self.dynamicArray[self.size] = n
        self.size += 1
            

    def popback(self) -> int:
        self.size -= 1
        return self.dynamicArray[self.size]

    def resize(self) -> None:
        length = len(self.dynamicArray)
        newArr = [None] * length * 2
        
        for i in range(self.size):
            newArr[i] = self.dynamicArray[i]
        self.capacity += length
        self.dynamicArray = newArr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity