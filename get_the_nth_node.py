class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
    i = 0
    while node:
        if i == index:
            return node
        node = node.next
        i += 1
    raise IndexError
