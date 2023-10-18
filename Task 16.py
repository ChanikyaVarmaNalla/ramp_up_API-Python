class QueueUsingStack:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        self.stack_enqueue.append(item)
        print(f"Element {item} enqueued.")

    def dequeue(self):
        if not self.stack_dequeue:
            if not self.stack_enqueue:
                print("Queue is empty. Cannot dequeue.")
                return None
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()

    def size(self):
        return len(self.stack_enqueue) + len(self.stack_dequeue)

    def display(self):
        if not self.stack_enqueue and not self.stack_dequeue:
            print("Queue is empty.")
        else:
            print("Elements in the queue:", self.stack_enqueue + self.stack_dequeue)


queue = QueueUsingStack()

while True:
    print("\nChoose an option:")
    print("1. Enqueue an element")
    print("2. Dequeue an element")
    print("3. Size of the queue")
    print("4. Display the queue")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        it = input("Enter the element to enqueue: ")
        queue.enqueue(it)
    elif choice == '2':
        it = queue.dequeue()
        if it:
            print(f"Dequeued element: {it}")
    elif choice == '3':
        print(f"Size of the queue: {queue.size()}")
    elif choice == '4':
        queue.display()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
