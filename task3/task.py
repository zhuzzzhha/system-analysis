import math

def main(adj_list):
    """
    Calculates graph entropy by its adjacency list.
    
    - param adj_list: adjacency list
    Returns graph entropy
    """
    vertex_degrees = {vertex: len(neighbors) for vertex, neighbors in adj_list.items()}
    total_edges_count = sum(vertex_degrees.values())
    
    if total_edges_count == 0:
        return 0
    entropy_value = 0
    for _, degree in vertex_degrees.items():
        if degree > 0:
            probability = degree / total_edges_count
            entropy_value -= probability * math.log2(probability)
    
    return entropy_value

example_graph = {
    '1': ['A', 'B'],
    '2': ['C', 'D', 'E'],
    '3': ['C', 'F', 'G'],
    '4': ['A'],
    '5': ['A'],
    '6': ['B'],
    '7': ['B']
}

entropy_of_graph = main(example_graph)
print(f"Graph entropy: {entropy_of_graph}")
