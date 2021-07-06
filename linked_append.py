class Node:
    def __init__(self,data= 'head', next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def append_at_begining(self,data):
        #node = Node(data, .head =memory locataion, .next = next nodes)
        node = Node(data, self.head.next)
        self.head.next = node
    
    def print_linked_list(self):
        
        if self.head.next is None:
            print("Linkedlist is Empty")
            return

        current_node = self.head
        res_str = ''
        while current_node.next != None:
            res_str = res_str + str(current_node) + " --> "
            current_node = current_node.next
        
        print(res_str)
    
    def add_at_end(self, data):
        if self.head.next == None:
            node = Node(data, None)
            self.head.next = node
            
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.append_at_begining(10)
    ll.append_at_begining(5)
    ll.print_linked_list()
    ll.add_at_end(20)
    ll.print_linked_list()

