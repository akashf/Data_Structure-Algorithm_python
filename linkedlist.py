# Append data to the tail of the list and prepend to the head
# Search the linked list for a value and return the node
# Remove a node
# Pop, which means to return the first node's value and delete the node from the list
# Insert data at some position in the list
# Return the size (length) of the linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def createLinkedList(lt):
    head = Node(0)
    tail = head
    for i in lt:
        tail.next = Node(i)
        tail = tail.next
    return head.next

def traverseList(hd):
    lstnew = []
    while hd:
        lstnew.append(hd.value)
        hd = hd.next
    return lstnew

def reverseList(hd):
    prev = None
    while hd:
        print(hd.value)
        temp = hd
        hd = hd.next
        temp.next = prev
        prev = temp
    return prev


#finding linked list is circular or not
#so if linked list is circular so it will point out prev nodes. 
# will use two pointers one move one time seconed two , if its not cirular 
#single node mover reach to end and never meet secord two step one, it cicular it will catchup with single one in iter

def isCircular(hd):
    if hd is None:
        return False
    fast, slow = hd, hd
    while fast and fast.next :
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            return True
    return False




lista = [4,2,5,1,-3,0]
print('list we have' , lista)
hd = createLinkedList(lista)
print('head of linkedlist', hd)
trverlist = traverseList(hd)
print("created list from linked", trverlist)
tempr = reverseList(hd)
print("revese list", traverseList(tempr))
print("revese list")

cl = createLinkedList([2, -1, 3, 0, 5])


# Creating a loop where the last node points back to the second node
loop_start = cl.next

while cl.next: 
    cl = cl.next   
cl.next = loop_start
# You will encouter the unlimited loop
# Click on stop
# Then right click on `clear outpit`
# while cl.next:
#     print(cl.val)
#     cl = cl.next
   
print('is linked list circular', isCircular(hd))
