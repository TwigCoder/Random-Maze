import random

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def generate_maze(width, height):
    if width % 2 == 0:
        width += 1
    if height % 2 == 0:
        height += 1

    maze = [["#"] * width for _ in range(height)]

    def carve_path(r, c):
        random.shuffle(DIRECTIONS)

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr * 2, c + dc * 2
            if 0 < nr < height and 0 < nc < width and maze[nr][nc] == "#":
                maze[nr][nc] = " "
                maze[r + dr][c + dc] = " "
                carve_path(nr, nc)

    start_row = random.randrange(1, height, 2)
    start_col = random.randrange(1, width, 2)
    maze[start_row][start_col] = "S"
    carve_path(start_row, start_col)

    end_edge = random.choice(["top", "bottom", "left", "right"])
    if end_edge == "top":
        end_row, end_col = 0, random.randrange(1, width, 2)
    elif end_edge == "bottom":
        end_row, end_col = height - 1, random.randrange(1, width, 2)
    elif end_edge == "left":
        end_row, end_col = random.randrange(1, height, 2), 0
    else:
        end_row, end_col = random.randrange(1, height, 2), width - 1

    maze[end_row][end_col] = "E"

    return maze, (start_row, start_col), (end_row, end_col)


def print_maze(maze):
    for row in maze:
        print("".join(row))


def is_valid_move(maze, row, col):
    if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
        return maze[row][col] != "#"
    return False


def to_json(maze):
    return maze
