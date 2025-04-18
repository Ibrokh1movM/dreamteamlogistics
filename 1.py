# Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([5, 12, 7, 9, 3], 7))  # Output: 2

print(linear_search([100, 200, 300, 400], 500))  # Output: -1

print(linear_search(['a', 'b', 'c', 'd'], 'c'))  # Output: 2

print(linear_search([1, 4, 6, 8, 10, 12], 8))  # Output: 3

print(linear_search([22, 33, 44, 55, 66], 66))  # Output: 4

print(linear_search([], 5))  # Output: -1


#
# Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 11], 7))  # Output: 3

print(binary_search([10, 20, 30, 40, 50, 60], 25))  # Output: -1

print(binary_search([2, 4, 6, 8, 10, 12, 14, 16], 16))  # Output: 7

print(binary_search([100, 200, 300, 400, 500], 300))  # Output: 2

print(binary_search([5], 5))  # Output: 0

print(binary_search([], 10))  # Output: -1



# Stack (LIFO)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())  # Output: 30

s.push(40)
print(s.peek())  # Output: 40

print(s.is_empty())  # Output: False

s.pop()
s.pop()
s.pop()
print(s.is_empty())  # Output: True

print(s.pop())  # Output: "Stack is empty"



# Queue (FIFO)


from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1

q.enqueue(4)
q.enqueue(5)
print(q.front())  # Output: 2

print(q.is_empty())  # Output: False

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print(q.is_empty())  # Output: True

print(q.dequeue())  # Output: "Queue is empty"



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print(None)
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def append(self, new_data):  # Oxiriga qo'shish
        node = Node(new_data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next  # c node
        current.next = node

    def prepend(self, data: str):  # Boshiga qo'shish
        new_node: Node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node: Node, data: str):
        if prev_node is None:
            print('Previous Node can not be None')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, key):
        current = self.head
        if current is not None and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def delete_at_position(self, position):
        if self.head is None:
            return
        current = self.head
        if position == 0:
            self.head = current.next
            current = None
            return
        for i in range(position - 1):
            current = current.next
            if current is None:
                break
        if current is None or current.next is None:
            return
        next_node = current.next.next
        current.next = None
        current.next = next_node

    def delete_head(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None

    def delete_tail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None


llist = LinkedList()
llist.append('Monday')
llist.append('Tuesday')
llist.append('Wednesday')
llist.append('Friday')
llist.prepend('Sunday')
llist.insert(llist.head.next.next.next, 'Thursday')

print("Original list:")
llist.display()

llist.delete('Tuesday')
print("\nAfter deleting 'Tuesday':")
llist.display()

llist.delete_at_position(2)
print("\nAfter deleting node at position 2:")
llist.display()

llist.delete_head()
print("\nAfter deleting head:")
llist.display()

llist.delete_tail()
print("\nAfter deleting tail:")
llist.display()