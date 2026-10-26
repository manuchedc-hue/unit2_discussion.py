"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Appending to the end of a list makes it the top of the stack,
        # ensuring the last item added is the first one removed (LIFO).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        if self.is_empty():
            print("Warning: Cannot pop from an empty stack.")
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek inspects the top item of the stack without mutating its state.
        if self.is_empty():
            print("Warning: Cannot peek an empty stack.")
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Appending to the right end maintains the arrival order for FIFO processing.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            print("Warning: Cannot dequeue from an empty queue.")
            return None
        # popleft() efficiently removes from the front in O(1) time
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Returns the next item in line to be dequeued without altering the queue.
        if self.is_empty():
            print("Warning: Cannot view front of an empty queue.")
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")

    # 1. Create a Stack object.
    my_stack = Stack()

    # 2. Add at least 4 values to the stack.
    print("\nPushing items [10, 20, 30, 40] onto the stack...")
    for val in [10, 20, 30, 40]:
        my_stack.push(val)

    print(f"Top item via peek(): {my_stack.peek()}")
    print("Demonstrating LIFO removal (Last In, First Out):")
    print(f"Popped: {my_stack.pop()}")  # Should be 40
    print(f"Popped: {my_stack.pop()}")  # Should be 30

    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    print("\nPushing items [10, 20, 30, 40] onto the stack...")
    for val in [10, 20, 30, 40]:
        my_stack.push(val)

    print(f"Top item via peek(): {my_stack.peek()}")
    print("Demonstrating LIFO removal (Last In, First Out):")
    print(f"Popped: {my_stack.pop()}")  # Should be 40
    print(f"Popped: {my_stack.pop()}")  # Should be 30

    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    print("\nTesting single-item stack edge case:")
    single_stack = Stack()
    single_stack.push(99)
    print(f"Pushed single item 99. Is stack empty? {single_stack.is_empty()}")
    print(f"Removed item: {single_stack.pop()}")
    print(f"Is stack empty after removal? {single_stack.is_empty()}")


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")
print("      test popping from an empty stack,")
print("      test peeking at an empty stack,")
print("      and verify a single-item stack becomes empty after removal.")

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
print("\n=== QUEUE DEMO ===")

# Requirements:
# 1. Create a Queue object.
my_queue = Queue()

# 2. Add at least 4 values to the queue.
print("\nEnqueuing items ['Alice', 'Bob', 'Charlie', 'Diana'] into the queue...")
for name in ['Alice', 'Bob', 'Charlie', 'Diana']:
    my_queue.enqueue(name)

print(f"Front item via front(): {my_queue.front()}")
print("Demonstrating FIFO removal (First In, First Out):")
print(f"Dequeued: {my_queue.dequeue()}")  # Should be 'Alice'
print(f"Dequeued: {my_queue.dequeue()}")  # Should be 'Bob'
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
print("\nEnqueuing items ['Alice', 'Bob', 'Charlie', 'Diana'] into the queue...")
for name in ['Alice', 'Bob', 'Charlie', 'Diana']:
    my_queue.enqueue(name)

print(f"Front item via front(): {my_queue.front()}")
print("Demonstrating FIFO removal (First In, First Out):")
print(f"Dequeued: {my_queue.dequeue()}")  # Should be 'Alice'
print(f"Dequeued: {my_queue.dequeue()}")  # Should be 'Bob'
# 5. Show what happens when dequeue() is used on an empty queue.
print("Testing empty queue operations:")
my_queue.front()
my_queue.dequeue()
print("Testing empty queue operations:")
my_queue.front()
my_queue.dequeue()

#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
print("Testing empty queue operations:")
my_queue.front()
my_queue.dequeue()

# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.
print("\nTesting single-item queue edge case:")
single_queue = Queue()
single_queue.enqueue("SoloItem")
print(f"Enqueued 'SoloItem'. Is queue empty? {single_queue.is_empty()}")
print(f"Removed item: {single_queue.dequeue()}")
print(f"Is queue empty after removal? {single_queue.is_empty()}")


if __name__ == "__main__":
    main()
