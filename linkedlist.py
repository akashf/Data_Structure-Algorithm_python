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

#createlinked list one time
def linkedlistCreation(listV):
    head = None  # Initialize head variable
    tail = None  # Initialize tail variable
    for i in listV:
        if head is None:
            head = Node(i)
            tail = head
        else:
            tail.next = Node(i)
            tail = tail.next
    return head

#function to convert linked list to list
def listCreationFromLinkedList(head):
    listV = []
    while head is not None:
        listV.append(head.value)
        head = head.next
    return listV

#function to prepend a value to linked list
def prepend(head, value):
    new_head = Node(value)
    new_head.next = head
    return new_head

#search for a value in linked list
def searchLinkedList(head, value):
    while head is not None:
        if head.value == value:
            return True
        else:
            head = head.next
    return False

#remove a node from element
def removeFromLinkedList(head, ele):
    if head.value == ele:
        return head.next
    current = head.next
    prev = head
    while current is not None:
        if current.value == ele:
            prev.next = current.next
            break
        prev = current
        current = current.next
    return head
        
        
#calculate length of linked list

def calculateLength(head):
    count = 0
    while head is not None:
        count = count+1
        head = head.next
    return count

#reverse the linked list
def reversList(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev



lista = [1,2,3,4,5]
head = linkedlistCreation(lista)
listP = listCreationFromLinkedList(head)
print(listP)

#list after prepand
prependhead = prepend(head, 0)
listPrepend = listCreationFromLinkedList(prependhead)
print(listPrepend)

#search for list
search = searchLinkedList(head, 9)
print("sttus of of the element", search )

#remove element from linked list
remove = removeFromLinkedList(head, 3)
listRemove = listCreationFromLinkedList(remove)
print(listRemove)


#calculate length of linked list
len = calculateLength(head)
print(len)

#revierse the linked list
reverse = reversList(head)
print(listCreationFromLinkedList(reverse))
