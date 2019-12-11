class UnionFind:
    def __init__(self, size):
        self.size = size
        self.num_components = size
        self.component_size = [1 for i in range(size)]
        self.ids = [i for i in range(size)]

    def find(self, p):
        root = p

        while root != self.ids[root]:
            root = self.ids[root]

        while p != self.ids[p] and self.ids[p] != root:
            next = self.ids[p]
            self.ids[p] = root
            p = next

        return root

    def unify(self, p, q):
        if self.is_connected(p, q):
            return

        root1 = self.find(p)
        root2 = self.find(q)

        if self.component_size[root1] > self.component_size[root2]:
            self.component_size[root1] += self.component_size[root2]
            self.ids[root2] = root1
        else:
            self.component_size[root2] += self.component_size[root1]
            self.ids[root1] = root2

        self.num_components -= 1

    def get_num_of_component(self):
        return self.num_components

    def get_component_size(self, p):
        return self.component_size[self.find(p)]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def get_size(self):
        return self.size


union_find = UnionFind(10)

union_find.unify(0, 1)
union_find.unify(1, 2)
union_find.unify(2, 3)
union_find.unify(3, 4)
union_find.unify(4, 5)

union_find.unify(6, 7)
union_find.unify(7, 8)
union_find.unify(8, 9)

print(union_find.find(4))
print(union_find.find(9))
print(union_find.get_num_of_component())
print(union_find.get_component_size(4))
print(union_find.get_component_size(9))
print(union_find.is_connected(4, 2))
print(union_find.is_connected(1, 8))
print("==============================")
union_find.unify(0, 9)
print(union_find.find(0))
print(union_find.find(9))
print(union_find.get_num_of_component())
print(union_find.get_component_size(0))
print(union_find.get_component_size(9))
print(union_find.is_connected(4, 2))
print(union_find.is_connected(1, 8))