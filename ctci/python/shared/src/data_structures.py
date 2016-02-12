class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
        
    def __init__(self):
        self.head = None

    def add(self, data):
        self.add_recursive(self.head, data)
        
    def add_recursive(self, head, data):
        if not head:
            self.head = Node(data)
        else:
            if head.next == None:
		head.next = Node(data)
	    else:
                self.add_recursive(head.next, data)

    def remove(self, data):
        self.remove_recursive(self.head, data)
        
    def remove_recursive(self, head, data):
        if head:
            if head == self.head and head.data == data:
                self.head = head.next
	    else:
                next_node = head.next
		if next_node and next_node.data == data:
                    head.next = next_node.next
                else:
		    self.remove_recursive(next_node, data)

    def add_arr(self, arr):
        for x in arr:
            self.add(x)
            
    def get_nth_node(self, n):
        curr_p = self.head
        if not curr_p or n < 0:
            return None
        
        while n != 0:
            if not curr_p.next:
                return None
            curr_p = curr_p.next
            n -= 1

        return curr_p
    
    def get_data(self):
        data = []
        curr = self.head
        while curr:
            data.append(curr.data)
            curr = curr.next
        return data
    
    def print_data(self):
        for data in self.get_data():
            print data
