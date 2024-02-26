class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(root):
    if not root:
        return

    if root.left:
        in_order_traversal(root.left)

    print(root.val)

    if root.right:
        in_order_traversal(root.right)


def main():
    # Define some test cases
    test_cases = [
        TreeNode(1, None, TreeNode(2, TreeNode(3), None)),
        TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))),
        TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6, TreeNode(7, TreeNode(8)))))))
    ]

    # Loop through each test case and print the result of the in-order traversal
    for i, root in enumerate(test_cases):
        print(f"Test case {i + 1}:")
        in_order_traversal(root)


if __name__ == "__main__":
    main()
