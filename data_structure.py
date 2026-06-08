class DoublyNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val 
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        pass