from edgegraph import *


# accepts a graph(GraphEL) & start vertex(VertexEL)
# returns list of vertices (VertexEL objects)
def dfs(graph, start):
    if graph is None or start is None:
        raise ValueError("Invalid graph or vertex")
        
    if start not in graph.vertices():
        return []
        
    visited = set()
    result = []
    
    def recursive_dfs(vertex):
        if vertex in visited:
            return
        else:
            visited.add(vertex)
            result.append(vertex)
            for neighbor in graph.adjacent(vertex):
                if neighbor not in visited:
                    recursive_dfs(neighbor)
                    
    recursive_dfs(start)
                    
    return result

            
if __name__ == "__main__":
    # file_graph = parse_graph_file("sample_graph")
    # start0 = file_graph.vertices()[0]
    # start1 = file_graph.vertices()[1]
    # start2 = file_graph.vertices()[2]
    # start3 = file_graph.vertices()[3]
    # print(dfs(file_graph, start1))
    
    file_graph = parse_graph_file("sample_graph2")
    start0 = file_graph.vertices()[0]
    start1 = file_graph.vertices()[1]
    start2 = file_graph.vertices()[2]
    start3 = file_graph.vertices()[3]
    start4 = file_graph.vertices()[4]
    start5 = file_graph.vertices()[5]
    print(dfs(file_graph, start5))
