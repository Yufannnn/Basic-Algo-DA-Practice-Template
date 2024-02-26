import random

class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.idx_map = {}

    def search(self, val):
        return val in self.idx_map

    def insert(self, val):
        if self.search(val):
            return False

        self.lst.append(val)
        self.idx_map[val] = len(self.lst) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False

        idx = self.idx_map[val]
        self.lst[idx] = self.lst[-1]
        self.idx_map[self.lst[-1]] = idx
        self.lst.pop()
        del self.idx_map[val]
        return True

    def getRandom(self):
        return random.choice(self.lst)


# Example usage
randomized_set = RandomizedSet()
print(randomized_set.insert(1))  # True
print(randomized_set.remove(2))  # False
print(randomized_set.insert(2))  # True
print(randomized_set.getRandom())  # 1 or 2 randomly
print(randomized_set.remove(1))  # True
print(randomized_set.insert(2))  # False
print(randomized_set.getRandom())  # 2
print(randomized_set.getRandom())  # 2
print(randomized_set.getRandom())  # 2