class DoublyNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val 
        self.next = next
        self.prev = prev

class DoublyLinkedList: # Danh sách liên kết đôi
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val):
        new_node = DoublyNode(val)

        if self.head is None: 
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    def prepend(self, val):
        new_node = DoublyNode(val)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def insert_at(self, index, val):
        if index < 0 or index > self.size:
            print("Lỗi: Index vượt quá giới hạn của danh sách!")
            return
        if index == 0:
            self.prepend(val)
            return
        if index == self.size:
            self.append(val)
            return

        new_node = DoublyNode(val)
        if index < self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - 1 - index):
                curr = curr.prev

        prev_node = curr.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = curr
        curr.prev = new_node

        self.size += 1
    
    def __len__(self):
        return self.size 

    def __iter__(self):
        current = self.head         
        while current is not None:  
            yield current.val       
            current = current.next  
