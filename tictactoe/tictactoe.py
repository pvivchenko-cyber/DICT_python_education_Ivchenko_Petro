def print_board(cells):
    print("---------")
    print(f"| {cells[0]} {cells[1]} {cells[2]} |")
    print(f"| {cells[3]} {cells[4]} {cells[5]} |")
    print(f"| {cells[6]} {cells[7]} {cells[8]} |")
    print("---------")


def check_win(cells, char):
    for i in range(0, 9, 3):
        if cells[i] == char and cells[i + 1] == char and cells[i + 2] == char:
            return True
    for i in range(3):
        if cells[i] == char and cells[i + 3] == char and cells[i + 6] == char:
            return True
    if cells[0] == char and cells[4] == char and cells[8] == char:
        return True
    if cells[2] == char and cells[4] == char and cells[6] == char:
        return True
    return False


def main():
    cells = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    print_board(cells)

    current_player = 'X'

    while True:
        coord_input = input("Enter the coordinates: > ").split()

        if len(coord_input) != 2 or not coord_input[0].isdigit() or not coord_input[1].isdigit():
            print("You should enter numbers!")
            continue

        row = int(coord_input[0])
        col = int(coord_input[1])

        if not (1 <= row <= 3) or not (1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        index = (row - 1) * 3 + (col - 1)

        if cells[index] != '_' and cells[index] != ' ':
            print("This cell is occupied! Choose another one!")
            continue

        cells[index] = current_player
        print_board(cells)

        # Перевірка стану гри
        x_wins = check_win(cells, 'X')
        o_wins = check_win(cells, 'O')

        if x_wins:
            print("X wins")
            break
        elif o_wins:
            print("O wins")
            break
        elif '_' not in cells and ' ' not in cells:
            print("Draw")
            break

        # Зміна гравця
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()