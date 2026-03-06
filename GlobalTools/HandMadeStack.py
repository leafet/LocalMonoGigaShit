class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None

    def __del__(self):
        pass

class HMStack:
    def __init__(self):
        self.Top = None
        self.Data = None

    def push(self, Data):
        node_to_add = Node(Data)

        if self.Top is None:
            self.Top = node_to_add

        node_to_add.Next = self.Top
        self.Top = node_to_add
        self.Data = Data

    def pop(self):
        if self.Top is None:
            return None

        node_to_get = self.Top
        self.Top = self.Top.Next

        data_to_return = node_to_get.Data

        del node_to_get

        return data_to_return

    def peek(self):
        if self.Top is None:
            return None
        return self.Top.Data