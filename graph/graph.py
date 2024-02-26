class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_edge(self, a: Node, b: Node):
        a.adjacent.append(b)
        b.adjacent.append(a)


    # Depth First Search

    # REQUIREMENTS
    # Traverse the graph and visit each node focusing on visiting deeper connections
    # before shallower connections
    # Return an array of values of the nodes visited in the order they were visited
        
    def depth_first_search(self, start_node: Node):
        # Use a stack to keep track of nodes to visit starting with start_node's
        # adjacency list.
        # Declare an array for values we've seen.
        
        # While the stack is not empty
        # Pop the top value off of the to_visit stack
        # Add this node's adjacent nodes to the to_visit stack,
        # if we haven't seen them already.
        # Add this node's value to the seen array.

        to_visit_stack = start_node.adjacent.copy()
        seen = [start_node.value]

        while len(to_visit_stack) > 0:
            this_node = to_visit_stack.pop()
            seen.append(this_node.value)

            for adjacent_node in this_node.adjacent:
                to_visit_vals = [node.value for node in to_visit_stack]
                if (adjacent_node.value not in to_visit_vals and
                    adjacent_node.value not in seen):
                    to_visit_stack.append(adjacent_node)

        return seen

    # Breadth First Search

    # REQUIREMENTS

    # Traverse the nodes in a graph from a starting node, searching all a node's
    # children before searching any of their descendants


    def breadth_first_search(self, start_node: Node):
        to_visit_queue = start_node.adjacent.copy()
        seen = [start_node.value]

        while len(to_visit_queue) > 0:
            this_node = to_visit_queue.pop(0) # O(n) // could be O(1) if we used a linked list
            seen.append(this_node.value)

            for adjacent_node in this_node.adjacent:
                to_visit_vals = [node.value for node in to_visit_queue]
                if (adjacent_node.value not in to_visit_vals and
                    adjacent_node.value not in seen):
                    to_visit_queue.append(adjacent_node)

        return seen
    
    # REQUIREMENTS
    # Find the shortest path between two nodes in a graph.
    # Return the minimum number of edges between the nodes.
    # Return None if one of the nodes isn't in the graph

    def shortest_distance(self, start: Node, seek: Node):
        # Implement breadth first search
        # Keep track of depth of search from start node.
        # Once we find the node we're looking for, return the depth.
 
        node_vals = [node.value for node in self.nodes]
        if (start.value not in node_vals or
            seek.value not in node_vals):
            return None
        
        to_visit_queue = [(start, 0)]
        seen = []

        while len(to_visit_queue) > 0:
            this_node, depth = to_visit_queue.pop(0) # O(n) // could be O(1) if we used a linked list

            if this_node.value == seek.value:
                return depth
            
            seen.append(this_node.value)

            for adjacent_node in this_node.adjacent:
                
                to_visit_vals = [node.value for node, depth in to_visit_queue]
                if (adjacent_node.value not in to_visit_vals and
                    adjacent_node.value not in seen):
                    to_visit_queue.append((adjacent_node, depth + 1))

    
# TEST CASE
    
if __name__ == "__main__":
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')

    graph = Graph()
    graph.add_nodes([a, b, c, d, e, f])

    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, c)
    graph.add_edge(c, d)
    graph.add_edge(e, d)
    graph.add_edge(c, e)
    graph.add_edge(e, f)

    seen_dfs_1 = graph.depth_first_search(a)
    if seen_dfs_1 != ["A", "C", "E", "F", "D", "B"]:
        print('ERROR! depth_first_search(a) should be ["A", "C", "D", "E", "F", "B"]')
        print(f"Instead got {seen_dfs_1}")

    seen_dfs_2 = graph.depth_first_search(d)
    if seen_dfs_2 != ["D", "E", "F", "C", "B", "A"]:
        print('ERROR! depth_first_search(d) should be ["D", "E", "F", "C", "B", "A"]')
        print(f"Instead got {seen_dfs_2}")

    seen_bfs_1 = graph.breadth_first_search(a)
    if seen_bfs_1 != ["A", "B", "C", "D", "E", "F"]:
        print('ERROR! depth_first_search(a) should be ["A", "B", "C", "D", "E", "F"]')
        print(f"Instead got {seen_dfs_1}")

    seen_bfs_2 = graph.breadth_first_search(d)
    if seen_bfs_2 != ["D", "C", "E", "A", "B", "F"]:
        print('ERROR! depth_first_search(d) should be ["D", "C", "E", "A", "B", "F"]')
        print(f"Instead got {seen_dfs_2}")

    min_dist_1 = graph.shortest_distance(a, d)
    if min_dist_1 != 2:
        print("ERROR! The minimum distance between a and d should be 2")
        print(f"Instead got {min_dist_1}")

    min_dist_2 = graph.shortest_distance(c, f)
    if min_dist_2 != 2:
        print("ERROR! The minimum distance between c and f should be 2")
        print(f"Instead got {min_dist_2}")