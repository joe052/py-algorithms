#    Main Author(s): Lovejeet Singh / Tanisha Sharma
#    Main Reviewer(s): Lovejeet Singh / Tansiha Sharma

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0


def get_overflow_list(grid):
    overflow_list = []
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell_value = abs(grid[row][col])
            neighbors_count = 0

            for dr, dc in neighbors:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and abs(grid[r][c]) >= cell_value:
                    neighbors_count += 1

            if cell_value >= neighbors_count:
                overflow_list.append((row, col))

    if not overflow_list:
        return None
    else:
        return overflow_list


def overflow(grid, a_queue):
    num_grids_added = 0

    while True:
        overflow_list = get_overflow_list(grid)

        if not overflow_list:
            break

        num_grids_added += 1
        new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for row, col in overflow_list:
            cell_value = grid[row][col]
            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in neighbors:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    new_grid[r][c] += 1
                    if cell_value < 0:
                        new_grid[r][c] = -abs(new_grid[r][c])

            new_grid[row][col] = 0

        a_queue.enqueue(new_grid)
        grid = new_grid

    return num_grids_added


if __name__ == "__main__":
    grid1 = [
        [-2, 2, -3, 0, 0],
        [0, -4, 0, 0, 0],
        [0, 0, 3, 0, 1],
        [-1, 0, 0, 0, 1]
    ]

    q1 = Queue()
    num_grids1 = overflow(grid1, q1)
    print(f"Number of grids added to the queue: {num_grids1}")

    grid2 = [
        [-1, 0, -1, -1, 0],
        [-1, 4, 4, 0, 0],
        [0, -1, 3, 0, 1],
        [-1, 0, 0, 0, 1]
    ]

    q2 = Queue()
    num_grids2 = overflow(grid2, q2)
    print(f"Number of grids added to the queue: {num_grids2}")