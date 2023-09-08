import heapq


def dijkstra(graph, start):
    distances = {}
    for node in graph:
        distances[node] = float("infinity")
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist < distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

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

    # Define a start node for your Dijkstra's algorithm
    start_node = 0

    # Call the Dijkstra's algorithm function and print the result
    result = dijkstra(graph, start_node)
    for node, distance in result.items():
        print(f"Distance from node {start_node} to node {node} is: {distance}")


if __name__ == "__main__":
    main()
