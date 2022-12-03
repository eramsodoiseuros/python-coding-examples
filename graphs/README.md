# Breadth First Search

This implementation of the `breadth-first search algorithm` will traverse the `graph` starting from the start node, printing each visited node as it goes. It uses a `queue` to keep track of which nodes to visit next, and a set to store the nodes that have already been visited to avoid visiting them again.

# Depth First Search

This implementation of the `depth-first search algorithm` will traverse the graph starting from the start node, printing each visited node as it goes. It uses a `stack` to keep track of which nodes to visit next, and a set to store the nodes that have already been visited to avoid visiting them again.

Note that the depth-first search algorithm is similar to the breadth-first search algorithm, but it uses a stack instead of a queue to keep track of which nodes to visit next. This means that the algorithm will visit all of the nodes in a particular branch of the graph before moving on to the next branch. This can be useful for certain types of search or traversal tasks, but it may not be the best approach for all scenarios.
# Controlled Flooding

This code defines a `Graph` class that represents a graph with a set of nodes and a dictionary of edges. The `add_node` and `add_edge` methods are used to add nodes and edges to the graph. The flood method is used to flood the graph with a message, starting from the specified source node.

The `flood` method uses a `breadth-first search algorithm` to traverse the graph, sending the message to each visited node. It uses a `queue` to keep track of which nodes to visit next, and a set to store the nodes that have already been visited to avoid sending the message to them again.

This implementation of `controlled flooding of messages` in a graph allows you to send a message to all nodes in the graph starting from a specified source node.