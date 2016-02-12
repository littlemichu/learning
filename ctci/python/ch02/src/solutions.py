# Questions from CTCI Chapter Two - Linked Lists
from sets import Set

from shared.src import data_structures

def reverse(data):
    for i in range(len(data) - 1, -1, -1):
        yield data[i]

# QUESTION 2.1
def remove_duplicates(linked):
    seen = Set()
    curr = linked.head
    while curr:
        if curr.data in seen:
            linked.remove(curr.data)
        else:
            seen.add(curr.data)
        curr = curr.next
    return

# QUESTION 2.2
# Assumptions:
#   1. linked has at least k + 1 nodes
#   2. k is an integer
#   3. k >= 0
#   4. k=0 --> returns last node
#   5. k=1 --> returns second to last node
def get_kth_to_last(linked, k):
    end_p = linked.head
    return_p = end_p

    # Increment end_p by k nodes
    for i in range(k):
        end_p = end_p.next

    # Increment both pointers until end_p hits the end
    # of the linked list
    while end_p.next:
        end_p = end_p.next
        return_p = return_p.next

    return return_p

# QUESTION 2.3
# Assumptions:
#   1. The node passed in is not the last node
def delete_node(node):
    if not node:
        return
    next_p = node.next
    node.data = next_p.data
    node.next = next_p.next

# QUESTION 2.4
def partition(linked, x):
    curr_p = linked.head
    while curr_p:
        # Skip first node because that can be in the intersection
        # of 'less than x' or '>= x'
        # Constantly checking next node so that you can delete it if needed
        
        next_p = curr_p.next
        # If next node is 'less than x', move next node to head
        if next_p and next_p.data < x:
            # Delete next node
            curr_p.next = next_p.next
                
            # Insert next node at head
            next_p.next = linked.head
            linked.head = next_p
            
        # Only move to next node if you already checked the next node
        else:  
            curr_p = curr_p.next

# QUESTION 2.5
def sum_linked_lists(linked1, linked2):
    linked_sum = data_structures.LinkedList()
    curr_p1 = linked1.head
    curr_p2 = linked2.head
    carry = 0

    # Loop through linked lists, adding values into linked_sum linked list
    while curr_p1 and curr_p2:
        # Calculate sum, accounting for carry
        curr_sum = curr_p1.data + curr_p2.data + carry
        carry = curr_sum/10
        linked_sum.add(curr_sum % 10)

        # Move to next node on both linked lists
        curr_p1 = curr_p1.next
        curr_p2 = curr_p2.next

    # Add remaining carry value if carry = 1
    if carry:
        linked_sum.add(1)

    return linked_sum

# Question 2.5 FOLLOW UP ----- START -----
def pad_with_zeroes(head1, head2):
    if not head1 or not head2:
        return None
    
    # Move across each linked lists at same pace until the end
    # of one linked list is reached
    curr_p1 = head1
    curr_p2 = head2
    while curr_p1 and curr_p2:
        curr_p1 = curr_p1.next
        curr_p2 = curr_p2.next

    # If one linked list is longer, pad the other with zeroes
    if curr_p1:
        while curr_p1:
            curr_p1 = curr_p1.next
            node = data_structures.Node(0)
            node.next = head2
            head2 = node
    elif curr_p2:
        while curr_p2:
            curr_p2 = curr_p2.next
            node = data_structures.Node(0)
            node.next = head1
            head1 = node
            
    return (head1, head2)

# Returns the head of the sum including the carry over
def sum_linked_lists_follow_up_recursive(head1, head2):
    if not head1 and not head2:
        return data_structures.Node(0)
    returned_head = sum_linked_lists_follow_up_recursive(head1.next, head2.next)

    # returned_head node contains carry for the next addition
    data_sum = head1.data + head2.data + returned_head.data

    # Move carry from new sum over to new head
    new_head = data_structures.Node(data_sum/10)
    new_head.next = returned_head

    # Store new sum minus carry in returned_head
    returned_head.data = data_sum % 10
    
    return new_head
    
def sum_linked_lists_follow_up(head1, head2):
    if not head1 or not head2:
        return None
    (head1, head2) = pad_with_zeroes(head1, head2)

    head = sum_linked_lists_follow_up_recursive(head1, head2)

    # Remove extra leading zero if such exists
    if head and not head.data:
        head = head.next

    linked_sum = data_structures.LinkedList()
    linked_sum.head = head
    return linked_sum

# Question 2.5 FOLLOW UP ----- END -----

# Question 2.6
def get_loop_start(head):
    seen = Set()
    while head:
        if head in seen:
            return head
        seen.add(head)
        head = head.next
    return None

# Question 2.7
def is_palindrome(head):
    if not head:
        return False
    
    stack = []
    slow_p = head
    fast_p = head

    # Move through linked list, pushing data onto the stack
    # until you reach this state:
    # There are N nodes (0, 1, ..., N-1)
    # N is even: slow_p will point to the node N/2 - 1 (node just before middle)
    # N is odd: slow_p will point to the node N/2 (middle node)
    while fast_p.next:
        stack.append(slow_p.data)
        fast_p = fast_p.next
        if not fast_p.next:
            break
        # Only move slow_p to next node if fast_p is able to make a full step
        slow_p = slow_p.next
        fast_p = fast_p.next
    
    # Move through rest of the linked list, popping values off the stack to
    # check if the remaining nodes are a reflection of the nodes already
    # traversed
    while slow_p.next:
        slow_p = slow_p.next
        if slow_p.data != stack.pop():
            return False

    return True
