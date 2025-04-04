def loop_size(node):
    slow, fast = node, node
    counter = 1
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            while slow != fast:
                counter += 1
                slow = slow.next
            return counter
    return 0
#ssggsgsg