class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        pass

class HMList:
    def __init__(self):
        self.head = None
        self.len = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.len += 1
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node
        self.len += 1

    def insert(self, index, data):
        if index < 0 or index > self.len:
            raise IndexError("Index out of range")

        node_to_add = Node(data)

        if index == 0:
            node_to_add.next = self.head
            self.head = node_to_add
            self.len += 1
            return

        current = self.head
        count = 0
        while count < index - 1:
            current = current.next
            count += 1

        node_to_add.next = current.next
        current.next = node_to_add
        self.len += 1

    def __getitem__(self, index):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of range")

        count = 0
        for item in self:
            if count == index:
                return item
            count += 1

        raise IndexError("Index has wrong format")

    def __setitem__(self, index, data):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of range")

        count = 0
        for item in self:
            if count == index:
                item.data = data
            count += 1

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next