import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

BOARD_SIZE = 120

def create_board():
    return np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

GLIDER_GUN = [
    (5, 1), (5, 2), (6, 1), (6, 2), (5, 11), (6, 11), (7, 11),
    (4, 12), (8, 12), (3, 13), (9, 13), (3, 14), (9, 14), (6, 15),
    (4, 16), (8, 16), (5, 17), (6, 17), (7, 17), (6, 18), (3, 21),
    (4, 21), (5, 21), (3, 22), (4, 22), (5, 22), (2, 23), (6, 23),
    (1, 25), (2, 25), (6, 25), (7, 25), (3, 35), (4, 35), (3, 36),
    (4, 36)
]

def rotate_90_cw(pattern):
    return [(y, -x) for x, y in pattern]

GLIDER_GUN_DOWN = rotate_90_cw(GLIDER_GUN)

def add_glider_gun(board, x, y, pattern):
    for dx, dy in pattern:
        board[x + dx, y + dy] = 1

def place_and_gate(board):
    add_glider_gun(board, 0, 80, GLIDER_GUN_DOWN)       # Glider gun 1
    add_glider_gun(board, 20, 99, GLIDER_GUN_DOWN)       # Glider gun 2
    add_glider_gun(board, 40, 120, GLIDER_GUN_DOWN)       # Glider gun 3

    # Place one glider gun shooting rightwards
    add_glider_gun(board, 10, 1, GLIDER_GUN)     # Glider gun

# Define the rules of the Game of Life
def update_board(board):
    new_board = board.copy()
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            # Count the number of alive neighbors
            num_alive_neighbors = np.sum(board[x-1:x+2, y-1:y+2]) - board[x, y]
            # Apply Conway's rules
            if board[x, y] == 1:
                if num_alive_neighbors < 2 or num_alive_neighbors > 3:
                    new_board[x, y] = 0
            else:
                if num_alive_neighbors == 3:
                    new_board[x, y] = 1
    return new_board

fig, ax = plt.subplots()
board = create_board()
place_and_gate(board)
img = ax.imshow(board, interpolation='nearest')

def animate(frame):
    global board
    board = update_board(board)
    img.set_data(board)
    return img,

ani = animation.FuncAnimation(fig, animate, frames=60, interval=0.1, blit=True)
plt.show()