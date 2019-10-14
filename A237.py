def print_list(node):
    print("[", end=" ")
    while node is not None:
        print(node, end=" ")
        node = node.next
    print("]")
    print()
