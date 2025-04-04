#1
# def sorted_insert(head, data):
#     new_node = Node(data)
#     current = head
#     while current.next is not None and current.data < data and current.next.data > data:
#         current = current.next
#     new_node.next = current.next
#     current.next = new_node
#     return head

#2
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    target = 0
    while current.next is not None:
        if target == 0 and current.data >= data:
            new_node.next = head
            return new_node
        if current.next.data > data:
            break
        current = current.next
        target += 1
    new_node.next = current.next
    current.next = new_node
    return head