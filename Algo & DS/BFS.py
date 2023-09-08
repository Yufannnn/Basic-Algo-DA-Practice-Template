def bfs(graph, start_node, visited):
    queue = [start_node]
    visited.append(start_node)

    while queue:
        curr = queue.pop(0)
        print(curr)

        for neighbor in graph[curr]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)


def main():
    # Define a more complex sample graph represented as an adjacency list
    graph = {
        0: [1, 3, 4],
        1: [2, 3, 5],
        2: [5, 6],
        3: [4, 6],
        4: [7],
        5: [7, 8],
        6: [8],
        7: [9],
        8: [9],
        9: []
    }

    # Define a start node for your BFS
    start_node = 0

    # Call the BFS function and print the result
    bfs(graph, start_node, [])


if __name__ == "__main__":
    main()
