##########################
# Depth first values
# return list in depth first traversal order
# travel value from left to right, high to low
# result as stack
#
#        a1
#    b2      c5
#  d3  e4      f6
#
# FILO, first in last out
#
# in_3
# in_2
# in_1
# Stack
# Output = [in_3, in_2, in_1]
#
# stack     curr     result
# a
# (c,b)     a    ->  a
# c,(e,d)   b    ->  a,b
# c,e       d    ->  a,b,d
# c         e    ->  a,b,d,e
# (f)       c    ->  a,b,d,e,c
#           f    ->  a,b,d,e,c,f
#
##########################
from Node import init_str_node as init_node


def iterative(root):
    # O(n) time
    # O(n) space
    if root is None:
        return []
    result = []
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        result.append(curr.val)  # a, b, d, e, f, c
        # first in last out
        # put right into stack first, then we can pop the left first
        if curr.right:
            stack.append(curr.right)  # c(f)
        if curr.left:
            stack.append(curr.left)  # b(d,e)

    return result


def recursive(root):
    # O(n) time
    # O(n) space
    if root is None:
        return []
    left_val = recursive(root.left)  # b(d, e)
    right_val = recursive(root.right)  # c(f)
    return [root.val, *left_val, *right_val]


def dfv_demo():
    print("### dfv_demo ###")
    print("Iterative:")
    print(iterative(init_node()))
    print("Recursive:")
    print(recursive(init_node()))
    print("##########################")
