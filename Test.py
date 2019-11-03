import heapq


class Item:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        if self.age == other.age:
            return self.name > other.name

        return self.age > other.age


pq = []
heapq.heapify(pq)
heapq.heappush(pq, Item("kevin", 29))
heapq.heappush(pq, Item("anthony", 29))
heapq.heappush(pq, Item("peter", 30))
heapq.heappush(pq, Item("zindex", 30))

for item in pq:
    print(item.name, item.age)