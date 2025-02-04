class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, other):
        dummy = Node(0)
        tail = dummy
        a, b = self.head, other.head

        while a and b:
            if a.data < b.data:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next

        tail.next = a if a else b
        self.head = dummy.next

    def merge_sort(self):
        if not self.head or not self.head.next:
            return self.head

        mid = self.get_middle()
        left_half = LinkedList()
        right_half = LinkedList()
        left_half.head = self.head
        right_half.head = mid.next
        mid.next = None

        left_half.merge_sort()
        right_half.merge_sort()
        self.sorted_merge(left_half)
        self.sorted_merge(right_half)

    def get_middle(self):
        slow, fast = self.head, self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Use
ll = LinkedList()
ll.append(4)
ll.append(2)
ll.append(5)
ll.append(1)
ll.append(3)

print("Оригінальний список:")
ll.print_list()

ll.reverse()
print("Реверсований список:")
ll.print_list()

ll.merge_sort()
print("Відсортований список:")
ll.print_list()
