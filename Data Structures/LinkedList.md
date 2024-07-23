# Linked List

## Table of Contents

1. [Linked List Overview](#linked-list-overview)
2. [Types of Linked Lists](#types-of-linked-lists)
   - 2.1. [Singly Linked List](#singly-linked-list)
   - 2.2. [Doubly Linked List](#doubly-linked-list)
   - 2.3. [Circular Linked List](#circular-linked-list)
3. [Components of a Linked List](#components-of-a-linked-list)
   - 3.1. [Node](#node)
   - 3.2. [Head](#head)
   - 3.3. [Tail](#tail)
4. [Basic Operations](#basic-operations)
   - 4.1. [Traversal](#traversal)
   - 4.2. [Insertion](#insertion)
   - 4.3. [Deletion](#deletion)
   - 4.4. [Searching](#searching)
   - 4.5. [Updating](#updating)
5. [Advantages of Linked Lists](#advantages-of-linked-lists)
6. [Disadvantages of Linked Lists](#disadvantages-of-linked-lists)
7. [Variants and Their Uses](#variants-and-their-uses)
   - 7.1. [Singly Linked List](#singly-linked-list-1)
   - 7.2. [Doubly Linked List](#doubly-linked-list-1)
   - 7.3. [Circular Linked List](#circular-linked-list-1)
8. [Applications of Linked Lists](#applications-of-linked-lists)
9. [Complexity Analysis](#complexity-analysis)
10. [Special Considerations](#special-considerations)
11. [Top 30 Linked List Questions](#top-30-linked-list-questions)

## Linked List Overview

A linked list is a linear data structure in which elements are not stored at contiguous memory locations. Instead, each element, called a node, contains a data part and a reference (or link) to the next node in the sequence. This structure allows for efficient insertion and deletion operations.

## Types of Linked Lists

1. **Singly Linked List**: Each node contains a single link field pointing to the next node.
2. **Doubly Linked List**: Each node contains two link fields, one pointing to the next node and one to the previous node.
3. **Circular Linked List**: The last node in the list points back to the first node, forming a circle.

## Components of a Linked List

1. **Node**: The fundamental building block of a linked list. It typically contains:
   - **Data**: The value stored in the node.
   - **Next**: A pointer/reference to the next node in the sequence.

2. **Head**: The first node in the linked list. The head is a reference to the first node and is crucial for accessing the list.

3. **Tail**: (Optional in singly linked lists but common in doubly linked lists and circular linked lists) A reference to the last node in the list.

## Basic Operations

1. **Traversal**: Moving through the nodes of the linked list starting from the head and proceeding to the next node using the next pointers until the end of the list is reached.

2. **Insertion**: Adding a new node to the list. This can occur at:
   - **Beginning**: Adjust the new node’s next pointer to point to the current head and update the head to be the new node.
   - **End**: Traverse to the last node and update its next pointer to the new node.
   - **Middle**: Traverse to the desired position and adjust pointers accordingly.

3. **Deletion**: Removing a node from the list. This can occur at:
   - **Beginning**: Update the head to point to the next node.
   - **End**: Traverse to the second-to-last node and update its next pointer to null.
   - **Middle**: Adjust pointers of the previous node to skip the node to be deleted.

4. **Searching**: Finding a node with a specific value by traversing through the list.

5. **Updating**: Changing the value of a node while maintaining the structure of the list.

## Advantages of Linked Lists

1. **Dynamic Size**: Linked lists can grow and shrink dynamically, unlike arrays which have a fixed size.
2. **Efficient Insertions/Deletions**: Insertions and deletions can be more efficient than in arrays, particularly at the beginning and end of the list.

## Disadvantages of Linked Lists

1. **Memory Overhead**: Each node requires extra memory for the pointer/reference.
2. **Sequential Access**: Linked lists do not support direct access to elements (as arrays do), requiring traversal from the head to the desired node.
3. **Cache Performance**: Linked lists can have poor cache performance compared to arrays due to non-contiguous memory storage.

## Variants and Their Uses

1. **Singly Linked List**: Used when only forward traversal is needed. Simpler and uses less memory per node compared to doubly linked lists.
2. **Doubly Linked List**: Used when bidirectional traversal is required. Common in scenarios like navigation systems (e.g., undo and redo operations).
3. **Circular Linked List**: Often used in applications where the list must be navigated in a loop, such as in round-robin scheduling or in the implementation of certain types of buffers.

## Applications of Linked Lists

1. **Dynamic Memory Allocation**: Linked lists are used in dynamic memory allocation schemes.
2. **Implementing Other Data Structures**: Many other data structures, such as stacks, queues, and graphs, can be implemented using linked lists.
3. **Undo Functionality in Software**: Applications that require the ability to undo operations often use linked lists.
4. **Real-time Systems**: Circular linked lists are used in real-time systems for task scheduling.

## Complexity Analysis

- **Insertion/Deletion at Beginning**: O(1)
- **Insertion/Deletion at End**: O(n) for singly linked lists (O(1) if tail reference is maintained), O(1) for doubly linked lists
- **Traversal/Search**: O(n)

## Special Considerations

- **Null References**: Proper handling of null references is crucial to avoid runtime errors.
- **Memory Management**: In languages without automatic garbage collection, memory management for dynamic allocation/deallocation is critical.
- **Pointer Operations**: Careful management of pointers is necessary to maintain list integrity during operations.

## Top 30 Linked List Questions

1. **What is a linked list?**
   - A linked list is a linear data structure where each element, called a node, contains a data part and a reference (or link) to the next node in the sequence. Unlike arrays, linked lists do not store elements in contiguous memory locations.

2. **What are the types of linked lists?**
   - **Singly Linked List**: Each node has a single link to the next node.
   - **Doubly Linked List**: Each node has two links, one to the next node and another to the previous node.
   - **Circular Linked List**: The last node points back to the first node, forming a circle.
   - **Circular Doubly Linked List**: Combines properties of both doubly linked and circular linked lists.

3. **What are the advantages of linked lists over arrays?**
   - Dynamic size: Linked lists can grow and shrink at runtime.
   - Ease of insertion/deletion: Inserting or deleting a node in a linked list is more efficient than in an array, where elements might need to be shifted.

4. **What are the disadvantages of linked lists compared to arrays?**
   - Memory overhead: Each node requires extra memory for storing pointers.
   - Random access: Linked lists do not support direct access to elements by index, which makes them slower for accessing elements compared to arrays.
   - Cache locality: Arrays have better cache locality, leading to better performance in some scenarios.

5. **Explain the structure of a node in a singly linked list.**
   - A node in a singly linked list contains two parts:
     - **Data**: The value or information stored in the node.
     - **Next**: A reference or pointer to the next node in the list.

6. **What is the head of a linked list?**
   - The head of a linked list is the first node in the list. It serves as the entry point to the list, and all operations on the list (such as traversal) start from the head.

7. **What is the tail of a linked list?**
   - The tail of a linked list is the last node, which typically points to null (in a singly linked list) or back to the head (in a circular linked list).

8. **How do you traverse a linked list?**
   - Traversal involves starting from the head and moving to the next node repeatedly until the end (null in a singly linked list or head in a circular linked list) is reached.

9. **What is the time complexity of searching for an element in a linked list?**
   - The time complexity for searching an element in a linked list is O(n), where n is the number of nodes in the list, as it requires a sequential search.

10. **What are the different ways to insert a node into a linked list?**
    - **At the beginning**: Adjust the new node's next pointer to the current head and then update the head to the new node.
    - **At the end**: Traverse to the last node, adjust its next pointer to the new node, and set the new node's next to null.
    - **After a given node**: Adjust the new node's next pointer to the given node's next, and then update the given node's next to the new node.
    - **Before a given node**: This typically involves finding the node preceding the given node and adjusting pointers accordingly.

11. **What is the time complexity of inserting a node in a linked list?**
    - Insertion at the beginning is O(1).
    - Insertion at the end or at a specific position requires traversal, making it O(n) in the worst case.

12. **How do you delete a node from a linked list?**
    - **From the beginning**: Adjust the head to point to the second node.
    - **From the end**: Traverse to the second-last node and set its next pointer to null.
    - **At a given position**: Adjust the previous node's next pointer to skip the node to be deleted and point to the next of the node being deleted.

13. **What is the time complexity of deleting a node in a linked list?**
    - Deletion at the beginning is O(1).
    - Deletion at the end or at a specific position requires traversal, making it O(n) in the worst case.

14. **Explain what a circular linked list is.**
    - A circular linked list is a variation where the last node points back to the first node, forming a circle. This allows for continuous traversal without reaching a null reference.

15. **What are the applications of linked lists?**
    - Dynamic memory allocation
    - Implementing data structures like stacks and queues
    - Managing resources in systems like file allocation tables
    - Implementing adjacency lists in graph representations

16. **What are the differences between singly and doubly linked lists?**
    - Singly linked lists have nodes with a single pointer to the next node, whereas doubly linked lists have nodes with pointers to both the next and previous nodes, allowing bidirectional traversal.

17. **What is a sentinel node in linked lists?**
    - A sentinel node (or dummy node) is an extra node that is not part of the list's actual data but simplifies boundary conditions. It's often used at the beginning (head sentinel) or end (tail sentinel) of the list.

18. **How does a doubly linked list handle deletion differently from a singly linked list?**
    - In a doubly linked list, you need to adjust the pointers of both the previous and next nodes of the node being deleted, making it more straightforward as you have direct access to the previous node.

19. **What is the time complexity of accessing an element by index in a linked list?**
    - The time complexity is O(n) because it requires traversing from the head to the desired index, unlike arrays which have O(1) access time.

20. **Can linked lists be used for implementing hash tables? If so, how?**
    - Yes, linked lists are often used to handle collisions in hash tables through chaining. Each bucket in the hash table contains a linked list to store all elements that hash to the same index.

21. **What are the memory usage implications of using linked lists?**
    - Linked lists use more memory than arrays due to the storage needed for pointers. Each node requires extra space for the reference(s) to other nodes.

22. **Explain the concept of a skip list.**
    - A skip list is a layered linked list that allows for faster search, insertion, and deletion by maintaining multiple levels of linked lists, with each level skipping over a fixed number of elements, thus reducing the search time complexity to O(log n).

23. **What is a circular doubly linked list?**
    - A circular doubly linked list is a combination of circular and doubly linked lists, where each node points to both its next and previous nodes, and the last node points back to the first node, forming a circular structure.

24. **How can linked lists be used to implement stacks?**
    - Linked lists can be used to implement stacks by maintaining the stack’s top as the head of the linked list. Push and pop operations are performed at the head of the list.

25. **How can linked lists be used to implement queues?**
    - Linked lists can be used to implement queues by maintaining pointers to both the front and rear of the list. Enqueue operations are performed at the rear and dequeue operations at the front.

26. **What is the advantage of using a circular linked list for implementing a queue?**
    - A circular linked list allows for efficient use of memory by reusing nodes and avoiding the need for shifting elements, which can enhance the performance of the queue operations.

27. **What is a self-referential structure in the context of linked lists?**
    - A self-referential structure is a structure that contains a pointer to an instance of the same structure. In linked lists, each node is an example of a self-referential structure as it points to the next node of the same type.

28. **How can you detect a cycle in a linked list?**
    - Cycles in a linked list can be detected using Floyd’s Cycle Detection algorithm, also known as the Tortoise and Hare algorithm. This involves using two pointers, one moving one step at a time and the other two steps at a time. If they meet, a cycle exists.

29. **What are the uses of the ‘next’ and ‘prev’ pointers in doubly linked lists?**
    - The ‘next’ pointer is used to traverse the list in a forward direction, while the ‘prev’ pointer allows traversal in the reverse direction, enabling more flexible operations such as reverse traversal and deletion.

30. **What is the difference between a linked list and an array in terms of data structure properties?**
    - **Memory allocation**: Linked lists use dynamic memory allocation, while arrays use static or dynamic memory in contiguous blocks.
    - **Access time**: Arrays provide O(1) time complexity for accessing elements, while linked lists provide O(n) due to sequential access.
    - **Insertion/deletion**: Linked lists offer efficient O(1) insertion and deletion at known positions, whereas arrays can have O(n) time complexity due to shifting elements.
    - **Memory overhead**: Linked lists have extra memory overhead for storing pointers, unlike arrays.
