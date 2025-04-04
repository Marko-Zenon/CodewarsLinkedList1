#1
# from preloaded import Node
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def push(head, data):
#     for _ in range(3):
#         new = Node(data)
#     return new

# def build_one_two_three():
#     # Your code goes here.
#     return Node(None)

#3
# from preloaded import Node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    head = None
    for i in range(3, 0, -1): 
        head = push(head, i)
    return head