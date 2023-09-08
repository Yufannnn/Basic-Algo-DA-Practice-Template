def khans_algorithm(graph):
    in_degree = {}
    for node in graph:
        in_degree[node] = 0

    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = []

    for node in in_degree:
        if in_degree[node] == 0:
            queue.append(node)

    topo_order = []

    while queue:
        curr = queue.pop(0)
        topo_order.append(curr)

        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    topo_order.append(neighbor)

    if len(topo_order) != len(graph):
        raise Exception("There is a cycle in the graph")

    return topo_order


def dfs(graph, start, visited):
    visited.add(start)
    stack = [start]
    top_order = []

    while stack:
        current = stack.pop()
        top_order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

    return top_order

def main():
    # Define a more complex sample graph represented as an adjacency list
    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4, 5],
        4: [5],
        5: [],
        6: [0, 2]  # Adding an extra node for complexity
    }

    # Call the Khan's algorithm function and print the result
    result = khans_algorithm(graph)
    result = dfs(graph, 6, set())
    if result:
        print("A possible topological ordering is:")
        print(result)

if __name__ == "__main__":
    main()
