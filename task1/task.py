import json
import sys

def get_edges(data, parent=None):
    edges = []
    for key, value in data.items():
        if parent is not None:
            edges.append((parent, key))
        if isinstance(value, dict):
            edges.extend(get_edges(value, key))
        elif isinstance(value, list):
            for item in value:
                edges.append((parent, item))
    return edges

def json_to_edges(input_file):
    with open(input_file, "r") as f:
        data = json.load(f)
        edges = get_edges(data)
        return edges

def edges_to_adjacency_matrix(edges):
    nodes = set()
    for edge in edges:
        nodes.update(edge)
    nodes = sorted(nodes)
    node_index = {node: index for index, node in enumerate(nodes)}

    size = len(nodes)
    matrix = [[0] * size for _ in range(size)]

    for edge in edges:
        start, end = edge
        matrix[node_index[start]][node_index[end]] = 1

    return matrix

def edges_to_adjacency_list(edges):
    adjacency_list = {}
    for start, end in edges:
        if start not in adjacency_list:
            adjacency_list[start] = []
        adjacency_list[start].append(end)
    return adjacency_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python task.py input_file.json")
        return

    input_file = sys.argv[1]
    edges = json_to_edges(input_file)
    print("Edges:", edges)

    adjacency_matrix = edges_to_adjacency_matrix(edges)
    print("Adjacency Matrix:")
    for row in adjacency_matrix:
        print(row)

    adjacency_list = edges_to_adjacency_list(edges)
    print("Adjacency List:")
    for node in sorted(adjacency_list):
        print(f"{node}: {adjacency_list[node]}")

if __name__ == "__main__":
    main()