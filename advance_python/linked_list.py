class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class linked_list_operation:
    def __init__(self):
        self.head= None
        self.tail= None

    def insertion_at_end(self, data):
        #Creating Node
        new_node = Node(data)
        if self.head == None:
            self.head=new_node
            self.tail=self.head
            return
        
        self.tail.next= new_node
        self.tail = new_node
    
    def insertion_at_start(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head=new_node
            self.tail=self.head
            return
        
        new_node.next = self.head
        self.head = new_node

    def delete_node_from_list(self,data):
        if self.head == None:
            return
        #in case of single node and that too equal to search node
        if self.tail.data == data and self.tail == self.head:
            self.head = None
            self.tail = self.head
            return

        current_node = self.head
        previous_node = None
        
        while current_node != self.tail.next:
            if current_node.data != data:
                previous_node=current_node
                current_node=current_node.next
            else:
                #in case of deleting first node, shift head pointer to next and preserve head pointer
                if current_node == self.head:
                    self.head =  self.head.next
                #in case of deleting last node, shift tail pointer to previous and preserve tail pointer
                elif current_node == self.tail:
                    self.tail = previous_node
                    previous_node.next= None    
                else:
                    previous_node.next = current_node.next
                return
                

    def print_linked_list(self):
        traverse = self.head
        if self.head == None:
            print("No data in present in the list")
            return
        print("Head", end="->")
        while traverse !=  self.tail:
            print(traverse.data, end="->")
            traverse = traverse.next
        print(self.tail.data, end="->None")

linked_list_operation_obj = linked_list_operation()
# linked_list_operation_obj.insertion_at_end(1)
# linked_list_operation_obj.insertion_at_end(11)
# linked_list_operation_obj.insertion_at_end(12)
# linked_list_operation_obj.insertion_at_end(15)
# linked_list_operation_obj.insertion_at_start(21)
# linked_list_operation_obj.insertion_at_end(20)
# linked_list_operation_obj.delete_node_from_list(12)
linked_list_operation_obj.print_linked_list()


    


        

