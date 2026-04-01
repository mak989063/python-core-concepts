def get_k_ele(head, k):
    temp = head
    for i in range(1, k):
        temp = temp.next

    return temp.data



