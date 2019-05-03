def create_board(height, width, board):
    """Render the game board as a 2D List

    :param height: the height of the board
    :param width: the width of the board
    """
    # Render the first row of indexes
    index_row = ""
    for n in range(1, width + 1):
        index_row += str(n)
    print(*index_row + ' ')

    # Render the game grid
    for x in range(height):
        row = []
        for y in range(width):
            row.append('#')
        board.append(row)
    for x in board:
        print(*x)


def player_move(width, x):
    """Request for player move

    :param width: the width of the board
    :param x: the column which the user wants to make a move in
    :return: returns x value
    """
    while x not in range(1, width + 1):
            try:
                # We have to handle this in a try catch block, because it may throw an exception
                x = int(input("Please enter your move\n"))
            except ValueError:
                # Make sure to handle a ValueError exception
                x = 0
    return x


def input_team():
    """ Get a team from the user
    :return: a character representing the user's chosen team
    """
    team_var = ''
    while team_var is not 'R' or 'Y':
        team_var = input("Choose a team, R for red or Y for yellow.\n").upper()

        if team_var == 'R' or team_var == 'Y':
            return team_var


def main():
    x = 0
    height = 6
    width = 7
    board = []
    input_team()
    create_board(height, width, board)
    player_move(width, x)


if __name__ == "__main__":
    # execute only if run as a script

    main()
