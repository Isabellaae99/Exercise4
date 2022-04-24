'''Class Template for a singly linked list Head -> Tail convention
Exercise Part starts at line 40'''


# class for holding the data, defaults to empty node if no data is given
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # pointer to the next node


# Class for managing the list and nodes
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1  # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    '''
    Exercise Part 1,2 and 3:

    Implement the given methods below according to the requirements in the exercise sheet.
    return the correct data types and values
    '''

    def clear(self):
        while self.head:
            temp = self.head
            self.head = self.head.next
            temp = None

    def get_data(self, data):
        if self.head == None:
            return False
        else:
            ret = False
            current = self.head
            while current.next:
                if current.data == data:
                    return current.data
                    ret = True
                current = current.next
            if current.data == data:
                return current.data
                ret = True
            if ret == False:
                return ret

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
            current = current.next


'''Exercise Part 4: Copy the code from the singly linked list implementation and rewrite it
    to implement a doubly linked list according to the exercise sheet. Dont forget to change the names of the classes
    in the code to reflect the new class name (NodeDLL instead of Node).
    '''


class NodeDLL:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.past = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = NodeDLL(data)
        self.tail = node

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            node.past = current
            current.next = node
        self.size += 1  # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    def clear(self):
        self.head = None
        self.size = 0

    def get_data(self, data):
        if self.head == None:
            return False
        else:
            ret = False
            current = self.head
            while current.next:
                if current.data == data:
                    return current.data
                    ret = True
                current = current.next
            if current.data == data:
                return current.data
                ret = True
            if ret == False:
                return ret

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.past = None
            self.size -= 1
        if self.tail.data == data:
            self.tail = self.tail.past
            self.tail.next = None
            self.size -= 1
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                current.next.next.past = current
                self.size -= 1
            current = current.next


class MyStack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, element):
        self.stack.append(element)
        self.size += 1

    def pop(self):
        return self.stack[self.size - 1]
        del self.stack[self.size - 1]
        self.size -= 1

    def top(self):
        return self.stack[self.size - 1]

    def size(self):
        return self.size


class MyQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def push(self, element):
        self.queue.append(element)
        self.size += 1

    def pop(self):
        return self.queue[0]
        del self.queue[0]
        self.size -= 1

    def show_left(self):
        return self.queue[0]

    def show_right(self):
        return self.queue[self.size - 1]

    def size(self):
        return self.size
