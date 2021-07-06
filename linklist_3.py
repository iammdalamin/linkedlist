


class Node:
    def __init__(self,data=None, next= None):
        self.data = data
        self.next = next
    
class Linkedlist:
    def __init__(self):
        self.head = Node()

    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node:
            cnt += 1
            current_node = current_node.next
            return cnt
            
    def append_at_begining(self, data):
        node = Node(data, self.head.next)
        self.head.next = node
    
    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
        
        current_node = self.head
        Info_str = ''

        while current_node:
            Info_str = Info_str + str(current_node.data)+ ' --> '
            current_node = current_node.next

        print(Info_str)

    def add_at_end(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = Node(data, None)
    
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            print("invalid Index")
            return
        
        if index == 0:
            self.append_at_begining(data)
            return
        
        cnt = 0
        current_node = self.head
        while current_node:
            if cnt == index - 1:
                node = Node(data, current_node.next)
                break
            current_node = current_node.next
            cnt += 1

if __name__ == '__main__':
    ll = Linkedlist()

    ll.append_at_begining(20)
    ll.append_at_begining(10)
    ll.print_linked_list()

    ll.add_at_end(30)
    ll.add_at_end(40)
    ll.print_linked_list()

    ll.insert_at(3,25)
    ll.insert_at(5, 35)
    ll.print_linked_list()