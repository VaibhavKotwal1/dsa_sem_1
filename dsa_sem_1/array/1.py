class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next  # Fix 1: Fixed typo 'teml' to 'temp'
            temp.next = new_node
            
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "\n")
            temp = temp.next

# Fix 2: Changed variable name to 'list1' to match usages below (avoiding 'list' keyword)
list1 = SLL() 

# Fix 3: Capitalised 'Node' because Python is case-sensitive
n1 = Node(10)  
n2 = Node(20)  

list1.append(n1)
list1.append(n2)  # Fix 4: Changed 'list2' to 'list1' (list2 was never created)
list1.append(Node(30))
list1.append(Node(40))

list1.print()  # Fix 5: Changed 'list1.print' from the original typo mapping