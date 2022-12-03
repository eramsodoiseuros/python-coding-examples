def depth_first_search(graph, start):
    # create a stack for tracking
    stack = []

    # create a set for storing visited nodes
    visited = set()

    # push the starting node onto the stack
    stack.append(start)

    # while there are nodes on the stack
    while stack:
        # pop the top node from the stack
        current = stack.pop()
        print(current)

        # if the node has not been visited
        if current not in visited:
            # mark the node as visited
            visited.add(current)

            # get the neighbors of the current node
            neighbors = graph[current]

            # push the neighbors onto the stack
            for neighbor in neighbors:
                stack.append(neighbor)


# test the depth-first search function
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

depth_first_search(graph, 'A')
