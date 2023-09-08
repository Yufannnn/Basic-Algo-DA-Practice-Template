def bellman_ford(graph, start):
    distances = {}
    for node in graph:
        distances[node] = float('infinity')
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise Exception("Negative cycle detected")

    return distances


def main():
    # Define a more complex sample graph represented as an adjacency list
    graph = {
        0: [(1, 1), (3, 4), (4, 2)],
        1: [(2, 2), (3, 2), (5, 3)],
        2: [(5, 1), (6, 4)],
        3: [(4, 3), (6, 1)],
        4: [(7, 1)],
        5: [(7, 2), (8, 3)],
        6: [(8, 2)],
        7: [(9, 1)],
        8: [(9, 3)],
        9: []
    }

    # Define a start node for your Bellman-Ford algorithm
    start_node = 0

    # Call the Bellman-Ford algorithm function and print the result
    result = bellman_ford(graph, start_node)
    if result:
        for node, distance in result.items():
            print(f"Distance from node {start_node} to node {node} is: {distance}")


if __name__ == "__main__":
    main()
