from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    # Enqueue element into queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to queue")

    # Safe dequeue method
    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
            return None
        else:
            return self.queue.popleft()

    # Display queue
    def display(self):
        print("Queue:", list(self.queue))


# -------- Driver Code --------
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Dequeued element:", q.safe_dequeue())
print("Dequeued element:", q.safe_dequeue())
print("Dequeued element:", q.safe_dequeue())

# Trying to dequeue from empty queue
print("Dequeued element:", q.safe_dequeue())