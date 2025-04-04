#1
# def swap_pairs(head):
#     if not head or not head.next:
#         return head
#     new = head
#     lst = []
#     while new is not None:
#         lst.append(new)
#         new = new.next
#     for i in range(0, len(lst), 2):
#         lst[i], lst[i + 1] = lst[i + 1], lst[i]
#     for i in range(len(lst) - 1):
#         lst[i].next = lst[i + 1]
#     lst[-1].next = None
#     return lst[0]
#2
def swap_pairs(head):
    if not head or not head.next:
        return head
    new = head
    lst = []
    while new is not None:
        lst.append(new)
        new = new.next
    if len(lst) % 2 == 0:
        for i in range(0, len(lst), 2):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    else:
        for i in range(0, len(lst) - 1, 2):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    for i in range(len(lst) - 1):
        lst[i].next = lst[i + 1]
    lst[-1].next = None
    return lst[0]
