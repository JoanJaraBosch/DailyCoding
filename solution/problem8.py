class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtrees(root):
    def helper(node):
        if not node:
            return 0, True  # Base case: (count, is_unival)

        left_count, is_left_unival = helper(node.left)
        right_count, is_right_unival = helper(node.right)

        # Check if the current node is a unival tree
        is_unival = is_left_unival and is_right_unival
        if node.left and node.left.val != node.val:
            is_unival = False
        if node.right and node.right.val != node.val:
            is_unival = False

        # If it's a unival subtree, increment count
        return (left_count + right_count + (1 if is_unival else 0)), is_unival

    count, _ = helper(root)
    return count

if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(0, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(0))

    print(count_unival_subtrees(root))  # Output: 5