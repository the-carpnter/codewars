def list_to_array(node):
    return [node.value] + list_to_array(node.next) if node else []
