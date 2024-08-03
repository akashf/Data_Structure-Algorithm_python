#build a stack using linked list
# build a stack using python list
# print stack push and pop
# balance paranthesis
# reverse stack

#building stack using linked list
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class stack:
    def __init__(self) -> None:
        self.head = None
        self.nextElement = 0


    def push(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            print("pushed ", self.head.value)
        else:
            temp.next = self.head
            print("pushed ", temp.value)
            self.head = temp
        self.nextElement += 1
    
    def traverse(self):
        while self.head:
            print("stack linked list ", self.head.value)
            self.head = self.head.next

    def pop(self):
        if self.head is None:
            return None
        else:
            item = self.head.value
            print("item poped", item)
            self.head = self.head.next
            self.nextElement -= 1
            return item
            
    def size(self):
        return self.nextElement
    

s = stack()
s.push(1)
s.push(4)
s.push(6)
s.push(10)
print('size of stack is', s.size())
s.pop()
s.pop()
s.pop()
s.traverse()

list1 = '[[]{}()]'
ls = stack()

pairs = {'(':')', '{':'}', '[':']'}

for i in list1:
    if i in pairs.keys():
        ls.push(i)
    elif i in pairs.values():
        if ls.nextElement == 0 or ls.pop() != i:
            print( False)

if ls.nextElement == 0:
    print( True)
else:
    print( False)


        
    


        