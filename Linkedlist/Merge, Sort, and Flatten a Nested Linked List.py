class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def LinkedList(a):
    head = Node(a[0])
    current = head
    for i in a[1:]:
        current.next = Node(i)
        current = current.next
    return head

def traverseLinkedList(hd):
    blk = []
    while hd:
        blk.append(hd.value)
        hd = hd.next
    return blk


a = [1,2,3,4,5,6]
head = LinkedList(a)
print("creating linked list",head.value )
print("traversal list", traverseLinkedList(head))