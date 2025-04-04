#1
# class Node(object):
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# def reverse(head, new_head=None):
#     if head is None:
#         return new_head
#     head.next = new_head
#     return reverse(head.next, head) 

#2
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_add(head, new_head=None):
    if head is None:
        return new_head
    next = head.next
    head.next = new_head
    return reverse_add(next, head)

def reverse(head):
    return reverse_add(head)