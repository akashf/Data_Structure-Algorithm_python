#reverse stack
class Node:
    def __init__(self, value) -> None:
        self.value = value  
        self.Next = None

class stack:
    def __init__(self) -> None:
        self.head = None
        self.noOfElement = 0
    
    def push(self, ele):
        temp = Node(ele)
        if self.head is None:
            self.head = temp
        else:
            temp.Next = self.head
            self.head = temp
        self.noOfElement += 1
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            temp = self.head.value
            self.head = self.head.Next
            self.noOfElement -= 1
        return temp
    
    
    def isEmpty(self):
        return self.noOfElement == 0 
    
    def top(self):
        if self.isEmpty():
            return None
        return self.head.value
        
    def size(self):
        return self.noOfElement
    
    def reverse(self):
        st = stack()
        while not self.isEmpty() :
            st.push(self.pop())
        return st
    
#lstInput = "}}{{"
#lstInput = "{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}"
lstInput = "}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{"
s = stack()


for i in lstInput:
    if s.isEmpty():
        s.push(i)
    else:
        top = s.top()
        if top == '{' and i == '}':
            s.pop()
        else:
            s.push(i)

count = 0

while not s.isEmpty():
    curr = s.pop()
    prev = s.pop()

    if prev == '}' and curr == '{' :
        print(curr, prev)
        count = count+2
    elif curr == '{' and prev == '{':
        count = count+1
    elif curr == '}' and prev == '}':
        count = count+1
    
print('Count is ', count)



    