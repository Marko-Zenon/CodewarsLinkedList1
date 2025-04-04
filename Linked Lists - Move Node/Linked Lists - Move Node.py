#1
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    moving_node = source
    source = source.next
    moving_node.next = dest
    dest = moving_node

    return Context(source, dest)