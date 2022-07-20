##########################
# Find target in tree, return True/False
##########################
from Node import init_str_node as init_node


def iterative(root, target):
    # O(n) time
    # O(n) space
    # bfs
    if root is None:
        return []
    queue = [root]
    while len(queue) > 0:
        curr = queue[0]
        queue = queue[1:]
        if curr.val == target:
            return True
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return False


def recursive(root, target):
    # O(n) time
    # O(n) space
    # dfs
    if root is None:
        return False
    if root.val == target:
        return True
    return recursive(root.left, target) or recursive(root.right, target)


def tree_inc_demo():
    target = "C"
    print("### tree_inc_demo ###")
    print("Iterative:")
    print(iterative(init_node(), target))
    print("Recursive:")
    print(recursive(init_node(), target))
    print("##########################")
