from typing import Optional
import sys
import json

class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        if not (lower < node.val < upper):
            return False
        return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

    return helper(root)

# Helper: Build tree from level-order list (with None for nulls)
def build_tree(data):
    if not data or data[0] is None:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in data]
    i = 0
    for j in range(1, len(data), 2):
        if nodes[i]:
            if j < len(data):
                nodes[i].left = nodes[j]
            if j + 1 < len(data):
                nodes[i].right = nodes[j + 1]
        i += 1
    return nodes[0]

# Input example: [5, 1, 4, None, None, 3, 6]
# Read from stdin or define manually
raw_input = sys.stdin.read().strip()
tree_data = json.loads(raw_input)
root = build_tree(tree_data)
print("true" if is_valid_bst(root) else "false")
