Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
    a. O(1)
    
2. What is the runtime complexity of `dequeue`?
    a. O(1)

3. What is the runtime complexity of `len`?
    a. O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
    a. O(logN)
2. What is the runtime complexity of `contains`?
    a. O(logN)
3. What is the runtime complexity of `get_max`? 
    a. O(logN)
## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?
    a. O(logN)

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
    a. O(1)

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
    a. O(1)
2. What is the runtime complexity of `ListNode.insert_before`?
    a. O(1)
3. What is the runtime complexity of `ListNode.delete`?
    a. O(1)
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    a. O(1)
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    a. O(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    a. O(1)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    a. O(1)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    a. O(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    a. O(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?
    a. O(1)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

   --The Linked list has a run time of O(1) since its runtime stays the same no matter the size of the list
   -- splice worst-case is O(n). This is because it has to change the index of every item in the array that gets moved. 