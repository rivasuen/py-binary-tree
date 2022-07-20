##########################
# sum all value stored in tree
##########################
from Node import init_num_node as init_node


def iterative(root):
    # O(n) time
    # O(n) space
    # bfs
    if root is None:
        return 0
    queue = [root]
    total = 0
    while len(queue) > 0:
        curr = queue[0]
        queue = queue[1:]
        total += curr.val

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return total


def recursive(root):
    # O(n) time
    # O(n) space
    # dfs
    if root is None:
        return 0

    return root.val + recursive(root.left) + recursive(root.right)


def tree_sum_demo():
    print("### tree_sum_demo ###")
    print("Iterative:")
    print(iterative(init_node()))
    print("Recursive:")
    print(recursive(init_node()))
    print("##########################")
