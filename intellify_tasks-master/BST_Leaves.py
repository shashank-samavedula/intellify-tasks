 
class Node: 
    
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None

def PrintLeaf(root): 
    s1 = [] 
    s2 = [] 

    s1.append(root) 

    while len(s1) != 0: 
        curr = s1.pop() 

        if curr.left: 
            s1.append(curr.left)  

        if curr.right: 
            s1.append(curr.right) 

        elif not curr.left and not curr.right: 
            s2.append(curr) 
    
    while len(s2) != 0: 
        print(s2.pop().val, end = " ") 


root = Node(15)
root.left = Node(10)
root.right = Node(26)
root.left.left = Node(8) 
root.right.left = Node(18) 
root.right.right = Node(33) 
root.left.right = Node(12)

PrintLeaf(root)

