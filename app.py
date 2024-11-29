from flask import Flask, render_template, jsonify, request
import maze

app = Flask(__name__)

player_pos = None
maze_data = None
start_pos = None
end_pos = None


@app.route("/")
def index():
    global player_pos, maze_data, start_pos, end_pos
    width, height = 21, 21
    maze_data, start_pos, end_pos = maze.generate_maze(width, height)
    player_pos = start_pos
    maze_json = maze.to_json(maze_data)
    return render_template("index.html", maze=maze_json, player_pos=player_pos)


@app.route("/new_maze")
def new_maze():
    global player_pos, maze_data, start_pos, end_pos
    width, height = 21, 21
    maze_data, start_pos, end_pos = maze.generate_maze(width, height)
    player_pos = start_pos
    maze_json = maze.to_json(maze_data)
    return jsonify(maze=maze_json, player_pos=player_pos)


@app.route("/move", methods=["POST"])
def move():
    global player_pos
    direction = request.json.get("direction")
    row, col = player_pos
    if direction == "up":
        new_row, new_col = row - 1, col
    elif direction == "down":
        new_row, new_col = row + 1, col
    elif direction == "left":
        new_row, new_col = row, col - 1
    elif direction == "right":
        new_row, new_col = row, col + 1
    else:
        return jsonify(error="Invalid direction"), 400

    if maze.is_valid_move(maze_data, new_row, new_col):
        player_pos = (new_row, new_col)

    if player_pos == end_pos:
        return jsonify(maze=maze.to_json(maze_data), player_pos=player_pos, win=True)

    return jsonify(maze=maze.to_json(maze_data), player_pos=player_pos)


if __name__ == "__main__":
    app.run(debug=True)
