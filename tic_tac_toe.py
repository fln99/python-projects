def how_to():
    print("How to play?")
    print("\nThe table is divided into 9 cells, 3 lines and 3 columns.\nThe diagram below illustrates the table and the coordinates:")
    print("\n   1  2  3\n1  _  _  _\n\n2  _  _  _\n\n3  _  _  _\n")


def render_table(table):
    for index, cell in enumerate(table):
        print(cell, end=" ")

        if index in [2, 5, 8]:
            print()


def insert_into_table(symbol, coordinates, table):
    index = ((coordinates[0] - 1) * 3) + coordinates[1] - 1

    if table[index] != "_":
        print("Position in the table already used.")
        return 1
    
    table[index] = symbol
    return 0


def prompt_coodinates():
    valid_coords = False

    while not valid_coords:
        try:
            x, y = map(int, input("coordinates #> ").strip().split())
        except ValueError:
            print("Please, only two numbers separated by a space.")
            continue

        if (x > 3 or x < 1) or (y > 3 or y < 1):
            print("Invalid coords.")
        else:
            valid_coords = True

    return (x, y)


def prompt_symbol():
    valid_symbols = False

    while not valid_symbols:
        symbol = input("symbol #> ").strip()[0].upper()

        if symbol not in "XO":
            print("Invalid symbol.")
        else:
            valid_symbols = True

    return symbol


def check_game_over(table, symbol):
    win_sequences = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    has_win = False
    i = 0

    while not has_win and i < len(win_sequences):
        a, b, c = win_sequences[i]

        if (table[a] + table[b] + table[c]) == symbol * 3:
            has_win = True

        i += 1

    return has_win


def main():
    print("- = [{  Welcome to Tic Tac Toe!  }] = -")
    how_to()

    table = ['_' for _ in range(9)]
    game_over = False

    render_table(table)

    try:
        while not game_over:
            user_coords = prompt_coodinates()
            user_symbol = prompt_symbol()

            insert_into_table(user_symbol, user_coords, table)
            game_over = check_game_over(table, user_symbol)
            render_table(table)

        if game_over:
            print(f"The game is over! {user_symbol} is the winner.")
    except KeyboardInterrupt:
        print("\nGame exit.")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()