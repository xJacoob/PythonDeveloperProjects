def game_not_finished(matrix_):
    for row in range(3):
        for col in range(3):
            if matrix_[row][col] == ' ':
                return True
    return False

def draw(matrix_):
    if game_not_finished(matrix_) is False and x_win(matrix_) is False and o_win(matrix_) is False:
        return True
    return False

def x_win(matrix_):
    row_win = [row for row in matrix_ if row == ['X', 'X', 'X']]
    col_win_v1 = [row[0] for row in matrix_]
    col_win_v2 = [row[1] for row in matrix_]
    col_win_v3 = [row[2] for row in matrix_]
    diagonal_win_v1 = [matrix_[i][i] for i in range(3)]
    diagonal_win_v2 = [matrix_[i][2 - i] for i in range(3)]
    if (row_win or col_win_v1 == ['X', 'X', 'X'] or col_win_v2 == ['X', 'X', 'X'] or col_win_v3 == ['X', 'X', 'X']
            or diagonal_win_v1 == ['X', 'X', 'X'] or diagonal_win_v2 == ['X', 'X', 'X']):
        return True
    return False


def o_win(matrix_):
    row_win = [row for row in matrix_ if row == ['O', 'O', 'O']]
    col_win_v1 = [row[0] for row in matrix_]
    col_win_v2 = [row[1] for row in matrix_]
    col_win_v3 = [row[2] for row in matrix_]
    diagonal_win_v1 = [matrix_[i][i] for i in range(3)]
    diagonal_win_v2 = [matrix_[i][2 - i] for i in range(3)]
    if (row_win or col_win_v1 == ['O', 'O', 'O'] or col_win_v2 == ['O', 'O', 'O'] or col_win_v3 == ['O', 'O', 'O']
            or diagonal_win_v1 == ['O', 'O', 'O'] or diagonal_win_v2 == ['O', 'O', 'O']):
        return True
    return False

def impossible(matrix_):
    count_X = 0
    count_O = 0
    for row in range(3):
        for col in range(3):
            if matrix_[row][col] == 'X':
                count_X += 1
            elif matrix_[row][col] == 'O':
                count_O += 1
            else:
                continue
    if x_win(matrix_) and o_win(matrix_) is True or abs(count_X - count_O) >= 2:
        return True
    return False

def matrix(user_input):
    matrix_list = []
    for row in range(3):
        matrix_list.append([])
        for col in range(3):
            index = row * 3 + col
            matrix_list[row].append(user_input[index])
    return matrix_list

def output(matrix_):
    print("---------")
    for row in range(3):
        print("|", end=' ')
        for col in range(3):
            print(matrix_[row][col], end=' ')
        print("|")
    print("---------")

def valid_data(matrix_):
    while True:
        move_input = input().split()
        try:
            x = int(move_input[0])
            y = int(move_input[1])
        except (ValueError, IndexError):
            print("You should enter numbers!")
            continue
        if x not in [1, 2, 3] or y not in [1, 2, 3]:
            print("Coordinates should be from 1 to 3!")
            continue
        row = x - 1
        col = y - 1
        if matrix_[row][col] == 'X' or matrix_[row][col] == 'O':
            print("This cell is occupied! Choose another one!")
            continue
        return row, col

def move_x(matrix_):
    row, col = valid_data(matrix_)
    matrix_[row][col] = 'X'
    return matrix_

def move_o(matrix_):
    row, col = valid_data(matrix_)
    matrix_[row][col] = 'O'
    return matrix_

def check(build_matrix):
    if impossible(build_matrix):
        return "Impossible"
    elif x_win(build_matrix):
        return "X wins"
    elif o_win(build_matrix):
        return "O wins"
    elif draw(build_matrix):
        return "Draw"
    elif game_not_finished(build_matrix):
        return "Game not finished"
    return False

build_matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
output(build_matrix)
while True:
    build_matrix = move_x(build_matrix)
    output(build_matrix)
    result = check(build_matrix)
    if result != "Game not finished":
        print(result)
        break
    build_matrix = move_o(build_matrix)
    output(build_matrix)
    if result != "Game not finished":
        print(result)
        break





