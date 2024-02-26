class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.rank[root_y] += self.rank[root_x]
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
            return True
        else:
            return False


def kruskals_algorithm(edges, n):
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(n)
    mst = []

    for edge in edges:
        u, v, w = edge
        if uf.union(u, v):
            mst.append(edge)

    return mst


def main():
    # Define a graph using an edge list (u, v, w) where u and v are nodes and w is the weight
    edges = [
        (0, 1, 1),
        (1, 2, 2),
        (2, 0, 2),
        (1, 3, 2),
        (3, 4, 3),
        (4, 2, 1),
    ]
    n = 5  # Number of nodes in the graph

    # Call the Kruskal's algorithm function and print the result
    mst = kruskals_algorithm(edges, n)
    print("The edges in the minimum spanning tree are:")
    for edge in mst:
        print(f"Edge from node {edge[0]} to node {edge[1]} with weight {edge[2]}")


if __name__ == "__main__":
    main()
