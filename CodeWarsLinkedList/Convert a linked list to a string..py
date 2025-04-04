# #1
# def stringify(node):
#     st = ''
#     while node is not None:
#         st += f'{node.data} -> '
#         node = node.next
#     return st
#2
def stringify(node):
    st = ''
    while node is not None:
        st += f'{node.data} -> '
        node = node.next
    return st + 'None'