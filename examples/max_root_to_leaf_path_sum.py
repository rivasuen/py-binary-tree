##########################
# Find the max sum path of tree
##########################
from Node import init_num_node as init_node


def recursive(root):
    # O(n) time
    # O(n) space
    # dfs
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val
    return root.val + max(recursive(root.left), recursive(root.right))


def max_root_to_leaf_path_sum_demo():
    print("### max_root_to_leaf_path_sum_demo ###")
    print("Recursive:")
    print(recursive(init_node()))
    print("##########################")
