class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            return

        self.vertex = vertex_id
        self.vertices[vertex_id] = set()



    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):

    family_tree =  Graph()

    for pair in ancestors:
        for ancestor in pair: 
           family_tree.add_vertex(ancestor)
           
        family_tree.add_edge(pair[0], pair[1])

    stack = [starting_node]
    depth = {}
    
    while len(stack) > 0:
        current_node = stack.pop()
        neighbors = family_tree.get_neighbors(current_node)
        
