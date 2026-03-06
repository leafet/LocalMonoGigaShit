class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HMStack:
    def __init__(self):
        self.top = None
        self.data = None

    def push(self, data):
        node_to_add = Node(data)

        if self.top is None:
            self.top = node_to_add

        node_to_add.next = self.top
        self.top = node_to_add
        self.data = data

    def pop(self):
        if self.top is None:
            return None

        node_to_get = self.top
        self.top = self.top.next

        data_to_return = node_to_get.data

        del node_to_get

        return data_to_return

    def peek(self):
        if self.top is None:
            return None
        return self.top.data