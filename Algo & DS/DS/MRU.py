class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class MRUCache:
    def __init__(self, capacity: int):
        self.cache = {}  # key -> node
        self.capacity = capacity
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node):
        prev, next = self.tail.prev, self.tail
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # Remove the MRU item, which is right after the head
            mru = self.head.next
            self.remove(mru)
            del self.cache[mru.key]

# Example usage
mru_cache = MRUCache(2)
mru_cache.put(1, 1)  # Cache is {1=1}
mru_cache.put(2, 2)  # Cache is {1=1, 2=2}
print(mru_cache.get(1))  # Returns 1, Cache is {2=2, 1=1}
mru_cache.put(3, 3)   # Evicts key 1, Cache is {1=1, 3=3}
print(mru_cache.get(2))  # Returns -1 (not found)
mru_cache.put(4, 4)   # Evicts key 3, Cache is {3=3, 4=4}
print(mru_cache.get(1))  # Returns -1 (not found)
print(mru_cache.get(3))  # Returns 3
print(mru_cache.get(4))  # Returns 4
