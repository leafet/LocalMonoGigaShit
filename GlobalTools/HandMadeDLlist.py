class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class HMDLList:
    def __init__(self):
        self.first = None
        self.last = None
        self.current = None
        self.len = 0

    def append(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.current = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
            self.current = new_node
        self.len += 1

    def insert(self, index, data):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of range")

        new_node = Node(data)

        if index < self.len // 2:
            current = self.first
            for _ in range(index):
                current = current.next
        else:
            current = self.last
            for _ in range(self.len - 1, index, -1):
                current = current.prev

        new_node.next = current.next
        new_node.prev = current

        if current.next is not None:
            current.next.prev = new_node
        else:
            self.last = new_node

        current.next = new_node

        self.len += 1
        return new_node

    def insert_after_current(self, data):
        new_node = Node(data)

        if self.current is None:
            self.first = new_node
            self.last = new_node
            self.current = new_node
        else:
            new_node.prev = self.current
            new_node.next = self.current.next

            if self.current.next is not None:
                self.current.next.prev = new_node
            else:
                self.last = new_node

            self.current.next = new_node
            self.current = new_node

        self.len += 1
        return new_node

    def __getitem__(self, index):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of range")

        if index < self.len // 2:
            current = self.first
            count = 0
            while count < index:
                current = current.next
                count += 1
        else:
            current = self.last
            count = self.len - 1
            while count > index:
                current = current.prev
                count -= 1

        return current

    def __setitem__(self, index, data):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of range")

        if index < self.len // 2:
            current = self.first
            count = 0
            while count < index:
                current = current.next
                count += 1
        else:
            current = self.last
            count = self.len - 1
            while count > index:
                current = current.prev
                count -= 1

        current.data = data

    def __iter__(self):
        current_node = self.first
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __len__(self):
        return self.len
