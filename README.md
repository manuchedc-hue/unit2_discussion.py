# Unit 2 Discussion: Stacks and Queues

## Project Overview
This project implements two fundamental linear data structures in Python: the **Stack** (Last In, First Out / LIFO) and the **Queue** (First In, First Out / FIFO). It demonstrates core structural behaviors, state manipulation, and robust edge-case handling for empty or single-item collections.

---

## Design Approach & Real-World Application Scenario

### 1. Stack Implementation (LIFO) & Scenario
Data Structure: Utilized a standard Python 'list' to store items.
Operations & LIFO Behavior:
    * 'push(value)': Appended items to the end of the list. This ensures the last item added sits at the top of the stack, making it the first one removed.
    * 'pop()': Removed and returned the last item.
    * 'peek()': Inspected the top item ('items[-1]') without mutating the stack.
* Real-World Application Scenario: A text editor's Undo/Redo history. When you type words or format text, each action is pushed onto a stack. When you press Ctrl+Z, the most recent action is popped and undone first (Last In, First Out).
* Edge Cases Handled:** Attempting to 'pop()' or 'peek()' on an empty stack triggers a safe warning message and returns 'None' rather than raising an unhandled 'IndexError'. Verified that a single-item stack successfully resets to an empty state after removal.

### 2. Queue Implementation (FIFO) & Scenario
Data Structure: Utilized 'collections.deque' for efficient O(1) appends and pops from both ends.
Operations & FIFO Behavior:
    * 'enqueue(value)': Added items to the right side of the deque, maintaining arrival order.
    * 'dequeue()': Removed and returned items from the left side ('popleft()'), ensuring the first item that arrived is the first one processed.
    * 'front()': Viewed the next item in line ('items[0]') without altering queue state.
* Real-World Application Scenario: A customer service ticketing system or coffee shop line. Customers are served strictly in the order they arrive (First In, First Out), preventing unfair wait times.
* Edge Cases Handled: Prevented errors during invalid operations by verifying 'is_empty()' before 'dequeue()' or 'front()' calls. Verified that a single-item queue becomes completely empty after its element is removed.

---

## Theoretical Memory Growth
Both data structures exhibit O(n) linear space complexity as they grow. Storing n items requires proportional memory allocation in the underlying Python list or deque, scaling directly with the number of elements added.

---


```bash

python unit2_discussion.py
