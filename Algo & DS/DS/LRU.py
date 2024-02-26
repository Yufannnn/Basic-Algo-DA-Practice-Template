class Node:
    # Node class for doubly linked list
    def __init__(self, key, value):
        self.key = key  # Key of the node
        self.value = value  # Value of the node
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

    def __str__(self):
        """
        String representation of the node.
        """
        return f"({self.key}, {self.value})"

class LRUCache:
    # Initialize the LRU Cache with a given capacity
    def __init__(self, capacity: int):
        self.cache = {}  # Dictionary to hold key-node pairs for O(1) access
        self.capacity = capacity  # Maximum capacity of the cache
        self.head = Node(0, 0)  # Dummy head node to mark the start of the linked list
        self.tail = Node(0, 0)  # Dummy tail node to mark the end of the linked list
        self.head.next = self.tail  # Initially, head points to tail...
        self.tail.prev = self.head  # ...and tail points back to head

    # Helper method to remove a node from the doubly linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next  # Grab references to the adjacent nodes
        prev.next, nxt.prev = nxt, prev  # Bypass the node to be removed

    # Helper method to insert a node right after the head
    def insert(self, node):
        prev, nxt = self.head, self.head.next  # Nodes immediately after the head
        prev.next = nxt.prev = node  # Insert the new node between head and the first node
        node.prev, node.next = prev, nxt  # Update the new node's pointers

    # Retrieve the value of the key if it exists, and mark it as recently used
    def get(self, key: int) -> int:
        if key in self.cache:  # Key found in cache
            self.remove(self.cache[key])  # Remove node from its current position
            self.insert(self.cache[key])  # Re-insert it right after head (mark as recently used)
            return self.cache[key].value  # Return the value of the node
        return -1  # Key not found in cache

    # Add a key-value pair to the cache or update if it already exists
    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # Key already in cache
            self.remove(self.cache[key])  # Remove the old node
        self.cache[key] = Node(key, value)  # Create a new node or update existing node in cache
        self.insert(self.cache[key])  # Insert it right after head (mark as recently used)

        if len(self.cache) > self.capacity:  # Check if cache exceeds capacity
            lru = self.tail.prev  # Least recently used node is right before tail
            self.remove(lru)  # Remove it from the linked list
            del self.cache[lru.key]  # Also remove it from the cache dictionary

    def __str__(self):
        """
        String representation of the cache.
        """
        return str({k: v.value for k, v in self.cache.items()})


def main():
    """
    Driver code to test the implementation.
    """
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    print(cache)  # Output: {1: 1, 2: 2, 3: 3}
    print(cache.get(2))  # Output: 2
    print(cache)  # Output: {1: 1, 3: 3, 2: 2}
    cache.put(4, 4)
    print(cache)  # Output: {3: 3, 2: 2, 4: 4}
    print(cache.get(1))  # Output: -1
    print(cache)  # Output: {3: 3, 2: 2, 4: 4}
    print(cache.get(3))  # Output: 3
    print(cache)  # Output: {2: 2, 4: 4, 3: 3}
    print(cache.get(4))  # Output: 4
    print(cache)  # Output: {2: 2, 3: 3, 4: 4}


if __name__ == "__main__":
    main()
