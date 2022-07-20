##########################
# Breadth first values
# return list in breadth first traversal order
# travel value from high to low, left to right
# result as queue
#
#        a1
#    b2      c5
#  d3  e4      f6
#
# FIFO, first in first out
# Queue int_1
# Queue int_2, int_1
# Queue int_3, int_2, int_1
# Output: [int_1, int_2, int_3]
#
# queue     curr     result
# a
# (c,b)     a    ->  a
# (e,d),c   b    ->  a,b
# (f),e,d   c    ->  a,b,c
# f,e       d    ->  a,b,c,d
# f         e    ->  a,b,c,d,e
#           f    ->  a,b,c,d,e,f
#
##########################
from Node import init_str_node as init_node


def iterative(root):
    # O(n) time
    # O(n) space
    if root is None:
        return []
    result = []
    queue = [root]
    while len(queue) > 0:
        curr = queue[0]
        queue = queue[1:]
        result.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return result


def bfv_demo():
    print("### bfv_demo ###")
    print("Iterative:")
    print(iterative(init_node()))
    print("##########################")
