class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None

    def __del__(self):
        pass

class HMList:
    def __init__(self):
        self.head = None
        self.Len = 0

    def append(self, Data):
        new_node = Node(Data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.Next is not None:
            last_node = last_node.Next

        last_node.Next = new_node
        self.Len += 1

    def insert(self, index, Data):
        node_to_add = Node(Data)

        if index > self.Len:
            raise IndexError("Index out of range")

        count = 0

        for item in self:
            if count == index - 1:
                target = item

                node_to_add.Next = target.Next
                target.Next = node_to_add
            count += 1

    def __getitem__(self, index):
        if index > self.Len:
            raise IndexError("Index out of range")

        count = 0

        for item in self:
            if count == index:
                return item
            count += 1

        raise IndexError("Index has wrong format")

    def __setitem__(self, index, Data):
        if index > self.Len:
            raise IndexError("Index out of range")

        count = 0

        for item in self:
            if count == index:
                item.Data = Data
            count += 1


    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.Next