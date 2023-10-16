#    Main Author(s): Tanisha Sharma 
#    Main Reviewer(s): Lovejeet Singh



class Stack:
    def __init__(self, cap=10):
        # Initialize the Stack with a given capacity (default is 10)
        self.capacity = cap
        self.data = [None] * cap  # Initialize a list with capacity
        self.size = 0

    def capacity(self):
        return self.capacity

    def push(self, data):
        # Add data to the top of the Stack
        if self.size == self.capacity:
            # If the stack is full, double the capacity
            self.capacity *= 2
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
            self.data = new_data
        self.data[self.size] = data
        self.size += 1

    def pop(self):
        # Remove and return the top element from the Stack
        if self.is_empty():
            raise IndexError('pop() used on an empty stack')
        self.size -= 1
        return self.data[self.size]

    def get_top(self):
        # Get the top element without removing it
        if self.is_empty():
            return None
        return self.data[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


class Queue:
    def __init__(self, cap=10):
        # Initialize the Queue with a given capacity (default is 10)
        self.capacity = cap
        self.data = [None] * cap  # Initialize a list with capacity
        self.size = 0
        self.front = 0

    def capacity(self):
        return self.capacity

    def enqueue(self, data):
        # Add data to the back of the Queue
        if self.size == self.capacity:
            # If the queue is full, double the capacity
            self.capacity *= 2
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[(self.front + i) % len(self.data)]
            self.data = new_data
            self.front = 0
        self.data[(self.front + self.size) % len(self.data)] = data
        self.size += 1

    def dequeue(self):
        # Remove and return the front element from the Queue
        if self.is_empty():
            raise IndexError('dequeue() used on an empty queue')
        front_data = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return front_data

    def get_front(self):
        # Get the front element without removing it
        if self.is_empty():
            return None
        return self.data[self.front]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


class Deque:
    def __init__(self, cap=10):
        # Initialize the Deque with a given capacity (default is 10)
        self.capacity = cap
        self.data = [None] * cap  # Initialize a list with capacity
        self.size = 0
        self.front = 0

    def capacity(self):
        return self.capacity

    def push_front(self, data):
        # Add data to the front of the Deque
        if self.size == self.capacity:
            # If the Deque is full, double the capacity
            self.capacity *= 2
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[(self.front + i) % len(self.data)]
            self.data = new_data
            self.front = 0
        self.front = (self.front - 1) % len(self.data)
        self.data[self.front] = data
        self.size += 1

    def pop_front(self):
        # Remove and return the front element from the Deque
        if self.is_empty():
            raise IndexError('pop_front() used on an empty deque')
        front_data = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return front_data

    def push_back(self, data):
        # Add data to the back of the Deque
        if self.size == self.capacity:
            # If the Deque is full, double the capacity
            self.capacity *= 2
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[(self.front + i) % len(self.data)]
            self.data = new_data
            self.front = 0
        self.data[(self.front + self.size) % len(self.data)] = data
        self.size += 1

    def pop_back(self):
        # Remove and return the back element from the Deque
        if self.is_empty():
            raise IndexError('pop_back() used on an empty deque')
        back_index = (self.front + self.size - 1) % len(self.data)
        back_data = self.data[back_index]
        self.size -= 1
        return back_data

    def get_front(self):
        # Get the front element without removing it
        if self.is_empty():
            return None
        return self.data[self.front]

    def get_back(self):
        # Get the back element without removing it
        if self.is_empty():
            return None
        back_index = (self.front + self.size - 1) % len(self.data)
        return self.data[back_index]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __getitem__(self, k):
        # Get the k'th value from the front of the Deque without removing it
        if k < 0 or k >= self.size:
            raise IndexError('Index out of range')
        return self.data[(self.front + k) % len(self.data)]


# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())  # Output: 3

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())  # Output: 1

    deque = Deque()
    deque.push_back(1)
    deque.push_back(2)
    deque.push_back(3)
    print(deque.pop_front())  # Output: 1