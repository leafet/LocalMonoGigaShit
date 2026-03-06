class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HMQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.data = None
        self.size = 0

    def enqueue(self, data):
        node_to_add = Node(data)

        if self.rear is None:
            self.front = node_to_add
            self.rear = node_to_add
        else:
            self.rear.next = node_to_add
            self.rear = node_to_add

        self.size += 1
        self.data = data

    def enqueue_by_node(self, node_to_add: Node):

        if self.rear is None:
            self.front = node_to_add
            self.rear = node_to_add
        else:
            self.rear.next = node_to_add
            self.rear = node_to_add

        self.size += 1
        self.data = node_to_add.data

    def dequeue(self):
        if self.front is None:
            return None

        node_to_get = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        data_to_return = node_to_get.data

        del node_to_get

        self.size -= 1
        return data_to_return

    def dequeue_by_node(self):
        if self.front is None:
            return None

        node_to_get = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        return node_to_get

    def peek(self):
        if self.front is None:
            return None
        return self.front.data