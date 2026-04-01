def print_nodes(head):
    temp = head

    while temp != None:
        print(temp.data, end=" ")
        temp = temp.next

    print()

