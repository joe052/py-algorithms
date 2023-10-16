class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0
    
# Instantiate the queue class
a_queue = Queue()

def get_overflow_list(grid):
    rows = len(grid)
    cols = len(grid[0])
    overflow_list = []

    for i in range(rows):
        for j in range(cols):
            neighbors = 0
            current_value = abs(grid[i][j])

            # Check all four possible neighbors (up, down, left, right)
            if i > 0:
                neighbors += 1
            if i < rows - 1:
                neighbors += 1
            if j > 0:
                neighbors += 1
            if j < cols - 1:
                neighbors += 1

            if current_value >= neighbors:
                overflow_list.append((i, j))

    if len(overflow_list) > 0:
        return overflow_list
    else:
        return None

# Example usage:
grid1 = [
    [2, 0, 0, 0, 0],
    [0, -3, 0, 0, 0],
    [0, 0, -2, 0, 0],
    [-1, 0, 0, 0, 3]
]

overflow_result1 = get_overflow_list(grid1)
print(overflow_result1)  # Output: [(0, 0), (3, 4)]

grid2 = [
    [-2, 0, 2, 0, 0],
    [0, -4, 0, -5, 0],
    [0, 0, -2, 0, 1],
    [-2, 0, 0, 0, 1]
]

overflow_result2 = get_overflow_list(grid2)
print(overflow_result2)  # Output: [(0, 0), (1, 1), (1, 3), (3, 0)]


def overflow(grid, a_queue):
    rows = len(grid)
    cols = len(grid[0])
    overflowing = False

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] < 0:
                # Cell is overflowing
                overflowing = True
                a_queue.enqueue((i, j))

    if not overflowing:
        return 0  # No overflowing cells, return 0

    while not a_queue.is_empty():
        i, j = a_queue.dequeue()
        neighbors = 0
        sign = 1 if grid[i][j] > 0 else -1  # Determine the sign of the overflowing cell

        # Check all four possible neighbors (up, down, left, right)
        if i > 0:
            neighbors += 1
            grid[i - 1][j] += sign
            if abs(grid[i - 1][j]) == abs(sign):
                a_queue.enqueue((i - 1, j))
        if i < rows - 1:
            neighbors += 1
            grid[i + 1][j] += sign
            if abs(grid[i + 1][j]) == abs(sign):
                a_queue.enqueue((i + 1, j))
        if j > 0:
            neighbors += 1
            grid[i][j - 1] += sign
            if abs(grid[i][j - 1]) == abs(sign):
                a_queue.enqueue((i, j - 1))
        if j < cols - 1:
            neighbors += 1
            grid[i][j + 1] += sign
            if abs(grid[i][j + 1]) == abs(sign):
                a_queue.enqueue((i, j + 1))

        grid[i][j] = 0

    return 1  # A new grid has been added to the queue

grid1 = [
    [-2, 2, -3, 0, 0],
    [0, -4, 0, 0, 0],
    [0, 0, 3, 0, 1],
    [-1, 0, 0, 0, 1]
]

result1 = overflow(grid1, a_queue)
print(result1)  # Output: 2

grid2 = [
    [-1, 0, -1, -1, 0],
    [-1, 4, 4, 0, 0],
    [0, -1, 3, 0, 1],
    [-1, 0, 0, 0, 1]
]

result2 = overflow(grid2, a_queue)
print(result2)  # Output: 3
