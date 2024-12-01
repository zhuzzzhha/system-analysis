import json

class Node:
    def __init__(self, val):
        self.val = val
        self.subordinates = []
        self.chief = None

def add_connection(chief, subordinate):
    chief.subordinates.append(subordinate)
    subordinate.chief = chief

def get_all_ancestors(node):
    ancestors = set()
    cur = node.chief
    while cur:
        ancestors.add(cur)
        cur = cur.chief
    return ancestors

def get_all_descendants(node):
    descendants = set()
    stack = [node]
    while stack:
        current = stack.pop()
        for subordinate in current.subordinates:
            descendants.add(subordinate)
            stack.append(subordinate)
    return descendants

def r1(node):
    return set(node.subordinates)

def r2(node):
    return {node.chief} if node.chief else set()

def r3(node):
    all_descendants = get_all_descendants(node)
    return all_descendants - r1(node)

def r4(node):
    all_ancestors = get_all_ancestors(node)
    return all_ancestors - r2(node)

def r5(node):
    if not node.chief:
        return set()
    siblings = set(node.chief.subordinates)
    siblings.discard(node)
    return siblings

def build_tree_from_json(json_string):
    data = json.loads(json_string)
    nodes = {}
    
    def create_node(key):
        if key not in nodes:
            nodes[key] = Node(key)
        return nodes[key]
    
    def traverse(data, chief_node=None):
        for key, value in data.items():
            current_node = create_node(key)
            if chief_node:
                add_connection(chief_node, current_node)
            traverse(value, current_node)
    
    traverse(data)
    return nodes

def main():
    test_string = '''{
        "1": {
            "2": {
                "3": {
                    "5": {},
                    "6": {}
                },
                "4": {
                    "7": {},
                    "8": {}
                }
            }
        }
    }'''
    
    nodes = build_tree_from_json(test_string)
    
    results = {}
    for node_key, node in nodes.items():
        results[node.val] = {
            "r1": len(r1(node)),
            "r2": len(r2(node)),
            "r3": len(r3(node)),
            "r4": len(r4(node)),
            "r5": len(r5(node))
        }
    
    print(f"{'Node':<3} {'r1':<20} {'r2':<20} {'r3':<20} {'r4':<20} {'r5':<20}")
    for node_key, info in sorted(results.items()):
        print(f"{node_key:<3} {str(info['r1']):<20} {str(info['r2']):<20} {str(info['r3']):<20} {str(info['r4']):<20} {str(info['r5']):<20}")

if __name__ == "__main__":
    main()
