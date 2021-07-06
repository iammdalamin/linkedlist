class Node:
    def __init__(self,data = 'head', next = None):
        self.data = data
        self.next = next
    
class Linkedlist:
    def __init__(self):
        self.head = Node()
    
    def appent_at_begining(self, data):
        node = Node(data,self.head.next)
        self.head.next = node
    
    def print_linked_list(self):
        if self.head is None:
            print('Linklist list is empty')
            return
        current_node = self.head
        res_str = ''
        while current_node != None:
            res_str = res_str + str(current_node.data) + " --> "
            current_node = current_node.next
        print(res_str)

    def append_at_end(self,data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = Node(data, None )

if __name__ == '__main__':
    ll = Linkedlist()
    ll.appent_at_begining(20)
    ll.appent_at_begining(10)
    ll.print_linked_list()
    ll.append_at_end(50)
    ll.print_linked_list()