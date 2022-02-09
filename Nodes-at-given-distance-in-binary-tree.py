# binary tree insertion

class Node :
    def __init__ ( self , data ) :
        self.left = None
        self.data = data
        self.right = None

class BinaryTree :
    def __init__ ( self ) : self.root = None
    
    def insert ( self , data ) :
        if self.root == None :
            self.root = Node ( data )
            return
        
        temp = self.root
        q = [ temp ]
        index = 0
        while index != len ( q ) :
            
            if temp == None : 
                temp = Node ( data )
                return
        
            if temp.data == data : return # data exists
        
            if temp.left : q.append ( temp.left )
            else :
                temp.left = Node ( data )
                return
        
            if temp.right : q.append ( temp.right )
            else : 
                temp.right = Node ( data )
                return
            
            index += 1
            temp = q [ index ]
            
        print ( " something unfathomable happened! " )
        return

    def printList ( self , node ) :
        if node == None : return
        if node.data : print ( node.data ) #data exists
        if node.left : 
            print ( " --- L of" , node.data , ":")
            self.printList ( node.left )
        if node.right : 
            print ( " --- R of" , node.data )
            self.printList ( node.right )
        return
    
    def toLinkedList ( self ) :
        if self.root == None : return
        linked_list = BinaryTree ()
        linked_list.root = Node ( self.root.data )
        q = linked_list.root
        a = [ self.root ]
        index = 0
        while index != len ( a ) :
            temp = a [ index ]
            if temp.left and temp.left not in a : 
                a.append ( temp.left )
                q.right = Node ( temp.left.data )
                q = q.right
            if temp.right and temp.right not in a : 
                a.append ( temp.right )
                q.right = Node ( temp.right.data)
                q = q.right
            index += 1
        return linked_list
    
    def toDoublyLinkedList ( self ) :
        if self.root == None : return
        parent = self.root
        node = self.root.right
        while node :
            node.left = parent
            node = node.right
            parent = parent.right
        self.root.left = parent
        return
    
    def printDoublyLinkedList ( self ) :
        if self.root == None : return
        print ( "left", "node" , "right" )
        print ( self.root.left.data ,"  ", self.root.data ,"  ", self.root.right.data )
        temp = self.root.right
        prev = self.root
        flag = self.root
        while temp != flag :
            print ( temp.left.data ,"  ", temp.data ,"  ", temp.right.data )
            temp = temp.right
        return

Obj = BinaryTree ()
arr = [ 5 , 8 , 3 , 2 , 6 , 4 , 9 , 1 , 7 ]
print ( "Tree ---->" )
for index , value in enumerate ( arr ) : Obj.insert ( value )
Obj.printList ( Obj.root )

print ( " " )
print ( "Single ---->" )
Obj = Obj.toLinkedList( )
Obj.printList ( Obj.root )

print ( " " )
print ( "Double ---->" )
Obj.toDoublyLinkedList ()
Obj.printDoublyLinkedList ()
