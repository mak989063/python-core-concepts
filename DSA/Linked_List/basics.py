#Basics
#Define a class
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


## Creating nodes
head = ListNode(1)
second = ListNode(2)
third = ListNode(3)

# Linking nodes
head.next = second
second.next = third

#Traversing
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" → ")
        temp = temp.next
    print("None")

"""
“A linked list is a dynamic data structure where each node contains data 
and a pointer to the next node, allowing efficient insertions and deletions.”
"""