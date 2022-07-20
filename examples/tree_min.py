##########################
# Find the min value from tree
##########################
from Node import init_num_node as init_node


def iterative(root):
    # O(n) time
    # O(n) space
    # dfs
    if root is None:
        return 0
    stack = [root]
    min_val = float('inf')
    while len(stack) > 0:
        curr = stack.pop()
        min_val = min(min_val, curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return min_val

    # bfs
    # if root is None:
    #     return 0
    # queue = [root]
    # min_val = float('inf')
    # while len(queue) > 0:
    #     curr = queue[0]
    #     queue = queue[1:]
    #     min_val = min(min_val, curr.val)
    #     if curr.left:
    #         queue.append(curr.left)
    #     if curr.right:
    #         queue.append(curr.right)
    # return min_val


def recursive(root):
    # O(n) time
    # O(n) space
    # dfs
    if root is None:
        return float('inf')
    return min(root.val, recursive(root.left), recursive(root.right))


def tree_min_demo():
    print("### tree_min_demo ###")
    print("Iterative:")
    print(iterative(init_node()))
    print("Recursive:")
    print(recursive(init_node()))
    print("##########################")
