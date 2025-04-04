#1
# def linked_list_from_string(s):
#     head = None
#     current = None
#     for i in s.split(" -> "):
#         if i is None:
#             node = Node(None)
#         else:
#             node = Node(int(i))
#         if head:
#             current.next = head
#             current = head
#         else:
#             head = node
#             current = head
#     return head

#2
def linked_list_from_string(s):
    head = None
    current = None
    for i in s.split(" -> "):
        if i == "None":
            continue
        node = Node(int(i))
        if head is None:
            head = node
            current = head
        else:
            current.next = node
            current = node
    return head
        