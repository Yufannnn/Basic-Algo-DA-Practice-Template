class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev

def print_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


def main():
    # Define some test cases
    test_cases = [
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        ListNode(1, ListNode(3, ListNode(5, ListNode(7, ListNode(9))))),
        ListNode(2, ListNode(4, ListNode(6, ListNode(8, ListNode(10))))),
    ]

    # Loop through each test case and print the original and reversed lists
    for i, head in enumerate(test_cases):
        print(f"Test case {i + 1}:")
        print("Original list: ", end="")
        print_list(head)

        reversed_head = reverse_list(head)

        print("Reversed list: ", end="")
        print_list(reversed_head)


if __name__ == "__main__":
    main()
