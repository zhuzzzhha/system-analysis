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

root = Node("root")
manager_1 = Node("manager_1")
manager_2 = Node("manager_2")
employee_1_1 = Node("employee_1_1")
employee_1_2 = Node("employee_1_2")
employee_2_1 = Node("employee_2_1")
employee_2_2 = Node("employee_2_2")

add_connection(root, manager_1)
add_connection(root, manager_2)
add_connection(manager_1, employee_1_1)
add_connection(manager_1, employee_1_2)
add_connection(manager_2, employee_2_1)
add_connection(manager_2, employee_2_2)

nodes = [root, manager_1, manager_2, employee_1_1, employee_1_2, employee_2_1, employee_2_2]
results = {}

for node in nodes:
    results[node.value] = {
        "r1": len(r1(node)),
        "r2": len(r2(node)),
        "r3": len(r3(node)),
        "r4": len(r4(node)),
        "r5": len(r5(node))
    }
    
print(f"{'Node':<3}{'r1':<20} {'r2':<20} {'r3':<20} {'r4':<20} {'r5':<20}")
for node, info in results.items():
    print(f"{node:<3} {str(info['r1']):<20} {str(info['r2']):<20} {str(info['r3']):<20} {str(info['r4']):<20} {str(info['r5']):<20}")
