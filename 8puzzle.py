import copy
from heapq import heappop, heappush

n = 3 #rows & cols
# Dir: down, left, up, right
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]
move_names = ["Down", "Left", "Up", "Right"]

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, k):
        heappush(self.heap, k)
    
    def pop(self):
        return heappop(self.heap)
    
    def empty(self):
        return len(self.heap) == 0

class Node:
    def __init__(self, parent, mat, emp_pos, cost, lvl, move=None):
        self.parent = parent
        self.mat = mat
        self.emp_pos = emp_pos
        self.cost = cost 
        self.lvl = lvl    
        self.move = move  

    def __lt__(self, nxt):
        return self.cost < nxt.cost

def calculate_manhattan_distance(mat, final) -> int:
    distance = 0
    final_positions = {value: (i, j) for i, row in enumerate(final) for j, value in enumerate(row) if value != 0}
    
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0:
                target_value = mat[i][j]
                if target_value in final_positions:
                    target_x, target_y = final_positions[target_value]
                    distance += abs(target_x - i) + abs(target_y - j)
    return distance

def new_node(mat, emp_pos, new_emp_pos, lvl, parent, final, move) -> Node:
    new_matrix = copy.deepcopy(mat)
    x1, y1 = emp_pos
    x2, y2 = new_emp_pos
    new_matrix[x1][y1], new_matrix[x2][y2] = new_matrix[x2][y2], new_matrix[x1][y1]
    cost = calculate_manhattan_distance(new_matrix, final)
    return Node(parent, new_matrix, new_emp_pos, cost, lvl + 1, move)

def matrix_printer(mat):
    for i in range(n):
        print(" ".join(str(mat[i][j]) for j in range(n)))

def is_safe(x, y):
    return 0 <= x < n and 0 <= y < n

def path_printer(root):
    if root is None:
        return
    path_printer(root.parent)
    if root.move:
        print(f"Move: {root.move}")
        print(f"F(X) = {root.lvl} + {root.cost}")
        matrix_printer(root.mat)

def get_matrix_input(matrix_name):
    while True:
        try:
            print(f"Enter the elements for the {matrix_name} matrix (3x3):")
            print("Represent the empty space with ' _ '")
            matrix = []
            unique_values = set()
            count = 0
            for i in range(n):
                row = list(map(str, input(f"Row {i + 1}: ").split()))
                if len(row) != n:
                    raise ValueError("Each row must have exactly 3 elements.")
                if any(row.count(x) > 1 for x in row):
                    raise ValueError("You cannot enter the same value more than once in a row.")
                if not unique_values.isdisjoint(row):
                    raise ValueError("All values must be unique.")
                for i in row:
                    if i == '_':
                        count+=1
                unique_values.update(row)
                matrix.append(row)
            if count != 1:
                raise ValueError("Matrix should contain only 1 Empty Tail ' _ '")
            return matrix
        except ValueError as e:
            print(f"Invalid input: {e}")

# def count_inversions(arr):
#     inversions = 0
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j] and arr[i] != 0 and arr[j] != 0:
#                 inversions += 1
#     return inversions

# def is_solvable(initial):
#     flat_list = [num for row in initial for num in row]
#     inversions = count_inversions(flat_list)
#     print(inversions)
#     return inversions % 2 == 0

def solver(initial, emp_pos, final):
    # if not is_solvable(initial):
        # print("The solution can't be determined for the given matrices.")
        # return
    
    pq = PriorityQueue()
    cost = calculate_manhattan_distance(initial, final)
    root = Node(None, initial, emp_pos, cost, 0)
    pq.push(root)

    visited = set()
    visited.add(tuple(map(tuple, initial)))

    while not pq.empty():
        m = pq.pop()
        if m.cost == 0:
            print("\nSolution found!")
            path_printer(m)
            return
        
        for i in range(4):
            new_tile_pos = [m.emp_pos[0] + row[i], m.emp_pos[1] + col[i]]
            if is_safe(new_tile_pos[0], new_tile_pos[1]):
                move = move_names[i]
                child = new_node(m.mat, m.emp_pos, new_tile_pos, m.lvl, m, final, move)
                if tuple(map(tuple, child.mat)) not in visited:
                    visited.add(tuple(map(tuple, child.mat)))
                    pq.push(child)
    print("No solution found for the given matrices.")

initial = get_matrix_input("initial")
final = get_matrix_input("final")

print("Initial matrix:")
matrix_printer(initial)
print("Final matrix:")
matrix_printer(final)

empty_tile_pos = next((i, j) for i in range(n) for j in range(n) if initial[i][j] == '_')

print("Solution to the Final state:", end=" ")
solver(initial, empty_tile_pos, final)
