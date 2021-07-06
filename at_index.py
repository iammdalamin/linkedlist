def insert_at(self, index, data):
    if index<0 or index>get_length():
        print('Invalid Index')
    
    if index == 0:
        self.append_at_begining(data)
        return

    cnt = 0
    current_node = self.head
    while current_node:
        if cnt == index - 1:
            node = Node(data, current_node.next)
            current_node.next = node
            break
        current_node = current_node.next
        cnt += 1