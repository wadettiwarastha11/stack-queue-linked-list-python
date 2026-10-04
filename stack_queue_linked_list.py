# Case Study: Stack and Queue Operations using Linked Lists

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ---------------- STACK USING LINKED LIST ----------------

class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into Stack")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            data = self.top.data
            self.top = self.top.next
            print(data, "popped from Stack")

    # Display Stack
    def display(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            temp = self.top
            print("Stack:", end=" ")
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")


# ---------------- QUEUE USING LINKED LIST ----------------

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into Queue")

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            data = self.front.data
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            print(data, "removed from Queue")

    # Display Queue
    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp = self.front
            print("Queue:", end=" ")
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")


# ---------------- MAIN PROGRAM ----------------

print("STACK OPERATIONS")
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.pop()
stack.display()


print("\nQUEUE OPERATIONS")
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()

queue.dequeue()
queue.display()