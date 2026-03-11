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
        self.len += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.current = new_node
        else:
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node
        self.len += 1

    def insert(self, index, data):
        if index < 0 or index > self.len:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(data)
            return

        if index == self.len:
            self.append(data)
            return

        new_node = Node(data)

        if index < self.len // 2:
            current = self.first
            count = 0
            while count < index:
                current = current.next
                count += 1
        else:
            current = self.last
            count = self.len - 1
            while count >= index:
                current = current.prev
                count -= 1

        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        self.len += 1

    def delete(self, index):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of range")

        node_to_delete = self.first
        count = 0
        while count < index:
            node_to_delete = node_to_delete.next
            count += 1

        if node_to_delete.prev is not None:
            node_to_delete.prev.next = node_to_delete.next
        else:
            self.first = node_to_delete.next

        if node_to_delete.next is not None:
            node_to_delete.next.prev = node_to_delete.prev
        else:
            self.last = node_to_delete.prev

        if self.current == node_to_delete:
            self.current = node_to_delete.next if node_to_delete.next else self.first

        self.len -= 1
        return node_to_delete.data

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

        return current.data

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

    def move_to_next(self):
        if self.current is not None and self.current.next is not None:
            self.current = self.current.next
            return True
        return False

    def move_to_prev(self):
        if self.current is not None and self.current.prev is not None:
            self.current = self.current.prev
            return True
        return False

    def get_current(self):
        if self.current is None:
            return None
        return self.current.data

    def set_current(self, index):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of range")
        self.current = self.first
        for _ in range(index):
            self.current = self.current.next

    def is_empty(self):
        return self.len == 0

    def clear(self):
        self.first = None
        self.last = None
        self.current = None
        self.len = 0
