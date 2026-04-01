def search(head, x):
    temp = head
    while temp != None:
        if temp.data == x:
            return True

        temp = temp.next

    return False