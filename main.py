import copy
import random


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


def get_ai_move(board, comp_team):
    """ Random generated computer move

    :param board:
    :param comp_team:
    :return:
    """
    a = random.randint(1, len(board))
    new_board = copy.deepcopy(board)
    assert 0 <= a - 1 < len(new_board[0])
    i = len(new_board) - 1
    while i >= 0:
        if new_board[i][a - 1] != '#':
            i = i - 1
        else:
            new_board[i][a - 1] = comp_team
            break
    return new_board


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


def play_move(board, player_team, move):
    """Renders the board with the users move
    :param board:
    :param player_team:
    :param move:
    :return:
    """
    new_board = copy.deepcopy(board)
    assert 0 <= move - 1 < len(new_board[0])
    i = len(new_board) - 1
    while i >= 0:
        if new_board[i][move - 1] != '#':
            i = i - 1
        else:
            new_board[i][move - 1] = player_team
            break
    return new_board


def render_board(board):
    """ Render a board to the console
    :param board:
    :return:
    """
    # Render the first row of indexes
    index_row = ""
    for n in range(1, len(board[0]) + 1):
        index_row += str(n)
    print(*index_row + ' ')
    # Renders the 2D array
    board_string = ""
    for row in board:
        row_string = ""
        for cell in row:
            row_string += cell + " "
        board_string += row_string + '\n'
    print(board_string)


def main():
    height = 6
    width = 7
    win_condition = False
    # Get the player's team
    player_team = input_team()
    print(player_team)
    comp_team = 'R' if player_team == 'Y' else 'Y'
    # Get a new empty board
    board = create_board(height, width)
    render_board(board)
    while win_condition is False:
        # Get the player's move
        move = player_move(width)
        print(move)

        # Plays the player's move
        board = play_move(board, player_team, move)
        render_board(board)

        # Plays a random computer move
        board = get_ai_move(board, comp_team)
        render_board(board)

    # TODO: repeat until the game ends


if __name__ == "__main__":
    # execute only if run as a script
    main()
