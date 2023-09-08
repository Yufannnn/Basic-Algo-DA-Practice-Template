class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = self.parent[y]
            self.rank[root_y] += self.rank[root_x]
        else:
            self.parent[root_y] = self.parent[x]
            self.rank[root_x] += self.rank[root_y]

def main():
    # Create a UnionFind object with 5 elements
    uf = UnionFind(5)

    # Define some test cases
    test_cases = [
        (0, 1),
        (1, 2),
        (3, 4)
    ]

    # Apply union operations according to the test cases
    for x, y in test_cases:
        uf.union(x, y)

    # Find and print the parent of each element
    for i in range(5):
        print(f"The representative of set containing {i} is: {uf.find(i)}")


if __name__ == "__main__":
    main()
