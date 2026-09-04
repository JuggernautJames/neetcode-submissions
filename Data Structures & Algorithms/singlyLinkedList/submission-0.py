class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index > self.size - 1:
            return -1
        element = self.head
        for i in range(index):
            element = element.next
        return element.value


    def insertHead(self, val: int) -> None:
        head = ListNode(val)
        if self.size == 0:
            self.head = head
            self.tail = head
        elif self.size == 1:
            self.head = head
            head.next = self.tail 
        else:
            next = self.head
            self.head = head
            head.next = next
        self.size += 1


    def insertTail(self, val: int) -> None:
        tail = ListNode(val)
        if self.size == 0:
            self.head = tail
            self.tail = tail
        elif self.size == 1:
            self.tail = tail
            self.head.next = tail
        else:
            prev = self.tail
            self.tail = tail
            prev.next = self.tail
        self.size += 1


    def remove(self, index: int) -> bool:
        if index > self.size - 1:
            return False
        element = self.head
        before = self.head
        for i in range(index):
            before = element
            element = element.next
        if index==0 and self.size==1:
            self.head = None
            self.tail = None
        elif index==0:
            self.head = self.head.next
        elif index==self.size-1:
            before.next = None
            self.tail = before
        else:
            before.next = element.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        ans = []
        element = self.head
        for i in range(self.size):
            ans.append(element.value)
            element = element.next
        return ans
        
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None