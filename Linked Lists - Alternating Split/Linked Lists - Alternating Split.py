#1
# class Node(object):
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class Context(object):
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second

# def alternating_split(head):
#     if not head or not head.next:
#         raise ValueError()
#     heads = [None, None]
#     currents = [None, None]
#     flag = 0
#     while head:
#         if heads[flag] is None:
#             heads[flag] = head
#             currents[flag] = head
#         else:
#             currents[flag].next = head
#             currents[flag] = head
#         flag = 1 - flag
#         head = head.next
#     return Context(heads[0], heads[1])



#2
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError()
    heads = [None, None]
    currents = [None, None]
    flag = 0
    while head:
        if heads[flag] is None:
            heads[flag] = head
            currents[flag] = head
        else:
            currents[flag].next = head
            currents[flag] = head
        flag = 1 - flag
        head = head.next
    if currents[0]:
        currents[0].next = None
    if currents[1]:
        currents[1].next = None
    return Context(heads[0], heads[1])