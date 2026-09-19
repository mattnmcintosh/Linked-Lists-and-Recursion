
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """Public wrapper for the recursive sum helper."""
        def _sum_helper(node):
            if node is None:
                return 0
            return node.data + _sum_helper(node.next)

        return _sum_helper(self.head)

    def recursive_reverse(self):
        """Public wrapper for the recursive in-place reversal helper."""
        def _reverse_helper(current, prev):
            if current is None:
                return prev
            next_node = current.next
            current.next = prev  # Re-point current node's next to previous
            return _reverse_helper(next_node, current)

        self.head = _reverse_helper(self.head, None)

    def recursive_search(self, target):
        """Public wrapper for the recursive search helper."""
        def _search_helper(node, target):
            if node is None:
                return False
            if node.data == target:
                return True
            return _search_helper(node.next, target)

        return _search_helper(self.head, target)

    def display(self):
        """Returns a string representation of the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "List is empty"
