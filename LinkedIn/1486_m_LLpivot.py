class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(start_node, k):
    before_start = ListNode(0)
    before = before_start

    after_start = ListNode(0)
    after = after_start

    while start_node:
        if start_node.val < k:
            before.next = start_node
            before = before.next
        else:
            after.next = start_node
            after = after.next

        start_node = start_node.next
        
    before.next = after_start.next
    after.next = None

    return before_start.next
    
def print_list(node):
    while node:
        print(node.val, end = " -> ")
        node = node.next
    print("None")

# Test
list_data = [5, 1, 8, 0, 3]
k = 3

# Creating linked list from the given list data
head = ListNode(list_data[0])
current = head
for i in range(1, len(list_data)):
    current.next = ListNode(list_data[i])
    current = current.next

print("Original List: ")
print_list(head)

new_head = partition(head, k)
print("\nPartitioned List:")
print_list(new_head)