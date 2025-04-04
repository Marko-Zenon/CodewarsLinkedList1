
#1
# from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
# def get_nth(node, index):
#     c = 0
#     while node is not None:
#         if c == index:
#             return node  
#         node = node.next
#         c += 1
#     return 

#3
from preloaded import Node
def get_nth(node, index):
    if node is None or index <0:
        raise IndexError
    c = 0
    while node is not None:
        if c == index:
            return node  
        node = node.next
        c += 1
    raise IndexError