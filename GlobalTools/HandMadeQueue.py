class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None

    def __del__(self):
        pass

class HMQueue:
    def __init__(self):
        self.Front = None
        self.Rear = None
        self.Data = None
        self.Size = 0

    def enqueue(self, Data):
        node_to_add = Node(Data)

        if self.Rear is None:
            self.Front = node_to_add
            self.Rear = node_to_add
        else:
            self.Rear.Next = node_to_add
            self.Rear = node_to_add

        self.Size += 1
        self.Data = Data

    def enqueue_by_node(self, node_to_add: Node):

        if self.Rear is None:
            self.Front = node_to_add
            self.Rear = node_to_add
        else:
            self.Rear.Next = node_to_add
            self.Rear = node_to_add

        self.Size += 1
        self.Data = node_to_add.Data

    def dequeue(self):
        if self.Front is None:
            return None

        node_to_get = self.Front
        self.Front = self.Front.Next

        if self.Front is None:
            self.Rear = None

        data_to_return = node_to_get.Data

        del node_to_get

        self.Size -= 1
        return data_to_return

    def dequeue_by_node(self):
        if self.Front is None:
            return None

        node_to_get = self.Front
        self.Front = self.Front.Next

        if self.Front is None:
            self.Rear = None

        self.Size -= 1
        return node_to_get

    def peek(self):
        if self.Front is None:
            return None
        return self.Front.Data