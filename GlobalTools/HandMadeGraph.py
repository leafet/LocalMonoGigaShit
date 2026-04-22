from collections import deque
class Vertex:
    def __init__(self, vid, graph):
        self.id = vid
        self.graph = graph
        self.data = None

    @property
    def degree(self):
        row = self.graph.matrix[self.id]
        return sum(row) + row[self.id]

class Graph:
    def __init__(self, matrix=None):
        if matrix is None:
            self.matrix = []
            self.vertices = []
            self.size = 0
        else:
            self.size = len(matrix)
            self.matrix = [row[:] for row in matrix]
            self.vertices = [Vertex(i, self) for i in range(self.size)]

    def reachable_within(self, start, max_steps):
        dist = [-1] * self.size
        q = deque([start])
        dist[start] = 0
        while q:
            v = q.popleft()
            d = dist[v]
            if d >= max_steps:
                continue
            for nb in range(self.size):
                if self.matrix[v][nb] and dist[nb] == -1:
                    dist[nb] = d + 1
                    q.append(nb)
        return [i for i in range(self.size) if dist[i] != -1]

