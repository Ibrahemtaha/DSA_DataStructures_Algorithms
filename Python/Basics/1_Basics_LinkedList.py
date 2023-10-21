class Node:
    def __init__(self,data):
        self.data = data
        self.ref  = None
        
#node1 = Node(1)
#print(node1)   
#//

class LinkedList:
    def __init__(self):
        self.head = None
  # Traversal       
    def print_LL(self):
        if self.head is None:
            print("LinkedList is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref
                
    # Add the New Node at the Beginning (Prepend)
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    # Add the New Node at the end    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
                
            

LL1 = LinkedList()
#LL1.add_begin(10)
LL1.add_end(100)
#LL1.add_end(500)
#LL1.add_begin(20)
LL1.print_LL()

# Create Node 

