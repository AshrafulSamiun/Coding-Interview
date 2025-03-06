class ListNode:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def int_to_dll(n: int) -> ListNode:
    # Handle negative numbers by placing the '-' at the front of the list
    if n < 0:
        head = ListNode('-')  # The sign node for negative numbers
        n = -n
    else:
        head = None
    
    # If number is 0
    if n == 0:
        return ListNode('0')

    # Create a list to store the digits as strings
    digits = []
    while n > 0:
        digits.append(str(n % 10))
        n //= 10
    
    # Reverse digits to maintain correct order
    digits.reverse()
    
    # Create the doubly linked list with digits in the correct order
    prev_node = head  # Start from the sign node (if negative)
    for digit in digits:
        current = ListNode(digit)
        if prev_node:
            prev_node.next = current
            current.prev = prev_node
        else:
            head = current
        prev_node = current
    
    return head

def dll_to_int(head: ListNode) -> int:
    # Convert doubly linked list to integer
    if not head:
        return 0

    sign = 1
    if head.value == '-':
        sign = -1
        head = head.next  # Skip the '-' sign node

    result = 0
    while head:
        result = result * 10 + int(head.value)
        head = head.next
    
    return sign * result

n = int(input())
head = int_to_dll(n)
# Doubly linked list representation: 2 <-> 5
print("First function output: ", end="")
node = head
while node:
    print(node.value, end=" <-> " if node.next else "")
    node = node.next
print()

# Convert back to integer:
reconstructed_number = dll_to_int(head)
print(f"Second function output: {reconstructed_number}")
