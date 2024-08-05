#build a queue using linked list



class Node:
    def __init__(self , value) -> None:
        self.value = value 
        self.next = None

class Queue:
    def __init__(self ) -> None:
        self.head = None
        self.tail = None
        self.noOfElement = 0

    def Enqueue(self, ele) :
        ne_node = Node(ele)
        if self.isEmpty():
            self.head = ne_node
            self.tail = self.head
        else:
            self.tail.next = ne_node
            self.tail = self.tail.next
        self.noOfElement += 1

    def Dequeue(self):
        if self.isEmpty():
            return None
        else:
            item = self.head.value
            self.head = self.head.next
            self.noOfElement -= 1
            return item
        
    def reverse(self):
        prev = None
        while self.head:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        return prev
    

    def size(self):
        return self.noOfElement
    
    def isEmpty(self):
        return self.noOfElement == 0
    

q = Queue()

lista = [1,2,3,4,5]

for i in lista:
    q.Enqueue(i)

pr = q.reverse()
while pr is not None:
    print(pr.value)
    pr = pr.next

