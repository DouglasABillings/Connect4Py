def create_board(height, width):
    """Return a new empty game board as a 2D List

    :param height: the height of the board
    :param width: the width of the board
    :return: an empty board
    """
    board = []
    for x in range(height):
        row = []
        for y in range(width):
            row.append('#')
        board.append(row)
    return board


def player_move(width):
    """Request for player move

    :param width: the width of the board
    :return: returns x value
    """
    move = 0
    while move not in range(1, width + 1):
        try:
            # We have to handle this in a try catch block, because it may throw an exception
            move = int(input("Please enter your move\n"))
        except ValueError:
            # Make sure to handle a ValueError exception
            move = 0
    return move


def input_team():
    """ Get a team from the user
    :return: a character representing the user's chosen team
    """
    team_var = ''
    while team_var is not 'R' or 'Y':
        team_var = input("Choose a team, R for red or Y for yellow.\n").upper()

        if team_var == 'R' or team_var == 'Y':
            return team_var


def render_board(board):
    """ Render a board to the console
    :param board:
    :return:
    """
    print("123456\n######\n######\netc...")


def main():
    height = 6
    width = 7

    # Get the player's team
    player_team = input_team()
    print(player_team)

    # Get a new empty board
    board = create_board(height, width)
    # TODO: this should be render_board(board) instead
    print(board)

    # TODO: render the board properly
    dumb_example_board = [['#', '#', '#'], ['#', '#', '#'], ['R', '#', 'Y']]
    render_board(board)
    render_board(dumb_example_board)

    # Get the player's move
    move = player_move(width)
    print(move)

    # TODO: modify the board with the player's move and render it again
    # TODO: get the AI's move
    # TODO: modify the board with the ai's move and render it again
    # TODO: repeat until the game ends


if __name__ == "__main__":
    # execute only if run as a script
    main()
