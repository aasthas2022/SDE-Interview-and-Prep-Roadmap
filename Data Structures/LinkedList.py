'''
Introduction: Create a linked list with three nodes and verify the data and next pointers of each node.
'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
     
head = None
tail = None   
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

head = one
one.next = two
two.next = three
tail = three

print(head.data, one.data, two.data, three.data, tail.data) # Output: 1 1 2 3 3
print(head.next.data, one.next.data, two.next.data, three.next) # Output: 2 2 3 None


'''
Traversing: Get the sum of all values from an integer linked list
'''

ans = 0
while head:
    ans += head.data
    head=head.next
print(ans) # Output = 6

'''
Insertion: Adding element at the start of linked list 
'''

def add_node_start(val):
    global head
    new_node = ListNode(val)
    new_node.next = head
    head = new_node
    
add_node_start(8)
    
print(head.data, head.next.data, one.next.data, two.next.data, three.next) # Output: 8 1 2 3 None

'''
Insertion: Adding element after a node in linked list
'''

def add_node_after(prev_node, val):
    new_node = ListNode(val)
    new_node.next = prev_node.next
    prev_node.next = new_node
    
add_node_after(two, 10)
print(head.data, one.next.data, two.next.data, three.next) # Output: 1 2 10 None

'''
Insertion: Adding element at the end of linked list
'''

def add_elem_end(val):
    new_node = ListNode(val)
    current = head
    while current.next:
        current = current.next
    
    current.next = new_node
    
add_elem_end(12)

print(head.data, one.next.data, two.next.data, three.next.data) # Output : 1 2 3 12

'''
Search: Search if element is in the linked list or not
'''

def search_elem(val):
    current = head
    while current.next:
        print(current.data)
        if current.data == val:
            return True
        current = current.next
    return False

print(search_elem(12))

'''
Find Length of a Linked List 
'''

def find_length_of_ll():
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

print(find_length_of_ll()) # Output: 3