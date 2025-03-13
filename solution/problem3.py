class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    """Encodes a tree to a single string."""
    if root is None:
        return "#"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"

def deserialize(data):
    """Decodes a single string back to a tree."""
    def helper(nodes):
        val = next(nodes)
        if val == "#":
            return None
        node = Node(val)
        node.left = helper(nodes)
        node.right = helper(nodes)
        return node
    
    nodes = iter(data.split(","))
    return helper(nodes)

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    print(deserialize(serialize(node)).left.left.val)
    print(deserialize(serialize(node)).left.left.val == 'left.left')