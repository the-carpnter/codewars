def length(head): 
    node = head
    count = 0
    while node:
        count += 1
        node = node.next
    return count
