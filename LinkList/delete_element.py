class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nodes(array, head):
    # Convert the array to a set for fast lookup
    remove_arr = set(array)
    
    # Create a dummy node to handle edge cases (e.g., removing the head node)
    dummy = ListNode(0)
    dummy.next = head
    current = dummy  # This will help traverse the list
    
    while current.next:
        if current.next.val in remove_arr:
            # Skip the node
            current.next = current.next.next
        else:
            current = current.next
    
    # Return the modified list starting from the original head
    return dummy.next

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(current.val)
        current = current.next
    print(result)

# Helper function to create a linked list from a list of values
def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example 1
array = [1, 2, 3]
linked_list = create_linked_list([1, 2, 3, 4, 5])
modified_linked_list = remove_nodes(array, linked_list)
print("Modified Linked List 1:")
print_linked_list(modified_linked_list)  # Output: [4, 5]

# Example 2
array = [5]
linked_list = create_linked_list([1, 2, 3, 4])
modified_linked_list = remove_nodes(array, linked_list)
print("Modified Linked List 2:")
print_linked_list(modified_linked_list)  # Output: [1, 2, 3, 4]
