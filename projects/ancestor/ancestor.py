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

    visited = []
    for i in get_parents(ancestors,starting_node):
        visited.append(i)
    while len(visited) > 0:
        node = visited.pop(0)
        for i in get_parents(ancestors,node):
            visited.append(i)
        if len(visited) == 0:
            return node
    return -1
    
def get_parents(dataset, children):
    parents = [node[0] for node in dataset if node[1] == children]
    parents.sort(reverse= True)
    return parents

