class Graph:
    def __init__(self, n=0):
        self.n = n
        self.adj_list = [[] for i in range(n)]

    def add_edge(self, fr, to, cost):
        self.add_directed_edge(fr, to, cost)
        self.add_directed_edge(to, fr, cost)

    def add_directed_edge(self, fr, to, cost):
        self.adj_list[fr].append([to, cost])

    def get_adj_list(self):
        return self.adj_list
