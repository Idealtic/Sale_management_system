class DoublyNode: # Nút trong danh sách liên kết đôi
    def __init__(self, val, next = None, prev = None):
        self.val = val 
        self.next = next
        self.prev = prev

class DoublyLinkedList: # Danh sách liên kết đôi
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val): # Thêm vào cuối danh sách
        new_node = DoublyNode(val)

        if self.head is None: 
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    def prepend(self, val): # Thêm vào đầu danh sách
        new_node = DoublyNode(val)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def insert_at(self, index, val): # Thêm vào index bất kỳ (bắt đầu từ 0)
        if index < 0 or index > self.size:
            print("Lỗi: Index vượt quá giới hạn của danh sách!")
            return
        if index == 0:
            return self.prepend(val)
        if index == self.size:
            return self.append(val)

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

    def remove_head(self): # Xoá phần tử đầu tiên của danh sách
        if self.head is None:
            return
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
    
    def remove_tail(self): # Xoá phần tử cuối cùng của danh sách
        if self.head is None:
            return
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1

    def remove_at(self, index): # Xoá phần tử bất kỳ của danh sách
        if index < 0 or index > self.size:
            print("Lỗi: Index vượt quá giới hạn của danh sách!")
            return
        if index == 0:
            return self.remove_head()
        if index == self.size - 1:
            return self.remove_tail()

        if index < self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - 1 - index):
                curr = curr.prev
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        self.size -= 1
    
    def __len__(self):
        return self.size 

    def __iter__(self):
        curr = self.head         
        while curr is not None:  
            yield curr.val       
            curr = curr.next  
