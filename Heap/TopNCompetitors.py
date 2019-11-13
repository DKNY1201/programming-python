import heapq
import unittest


def top_n_competitor(top_n_comps, comps, reviews):
    if not top_n_comps or not comps or not reviews:
        return []

    comps_mention = dict()

    for comp in comps:
        comps_mention[comp] = 0

    for review in reviews:
        for word in review.split(" "):
            word = word.lower()
            if word in comps_mention:
                comps_mention[word] += 1

    pq = []
    heapq.heapify(pq)

    for key, val in comps_mention.items():
        heapq.heappush(pq, Comp(key, val))

    return [shop.name for shop in heapq.nsmallest(top_n_comps, pq)]


class Comp:
    def __init__(self, name, num_mentioned):
        self.name = name
        self.num_mentioned = num_mentioned

    def __lt__(self, other):
        # sorted by num_mentioned descending first then name ascending
        return self.name < other.name if self.num_mentioned == other.num_mentioned else self.num_mentioned > other.num_mentioned


class Test(unittest.TestCase):
    def test_n_competitors(self):
        top_n_comps = 2
        comps = ["newshop", "shopnow", "afshion", "fashionbeats", "mymarket", "tcellular"]
        reviews = ["newshop is providing good service in the city;everyone should try newshop",
                   "best services by newshop",
                   "fashionbeats has great services in the city",
                   "Im proud to have fashionbeats",
                   "mymarket has awesome service",
                   "thank Newshop for the quick delivery"]
        self.assertEqual(top_n_competitor(top_n_comps, comps, reviews), ["newshop", "fashionbeats"],
                         "Should return top competitors that have mentioned most in review")

        top_n_comps = 2
        comps = ["newshop", "shopnow", "afshion", "fashionbeats", "mymarket", "tcellular"]
        reviews = ["newshop is providing good service in the city;everyone should try newshop",
                   "best services by newshop",
                   "fashionbeats has great services in the city",
                   "Im proud to have fashionbeats",
                   "afshion has awesome service",
                   "thank afshion for the quick delivery"]
        self.assertEqual(top_n_competitor(top_n_comps, comps, reviews), ["newshop", "afshion"],
                         "Should return top competitors that have mentioned most in review. "
                         "If there is same mentioned number, get the one appear first in alphabetical table")
