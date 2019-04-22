def render_board(height, width):
    """Render the game board

    :param height: the height of the board
    :param width: the width of the board
    """
    # Render the first row of indexes
    index_row = ""
    for n in range(1, width + 1):
        index_row += str(n)
    print(index_row)

    # Render the game grid
    board = '#' * width
    for i in range(1, height + 1):
            print(board)


def player_move(width):
    """Request for player move

    :param width: the width of the board
    :return: returns x value
    """
    # tuple for user prompt
    x = 99
    while x not in range(1, width + 1):
            try:
                # We have to handle this in a try catch block, because it may throw an exception
                x = int(input("Please enter your move\n"))
            except ValueError:
                # Make sure to handle a ValueError exception
                x = 99
    return x


def main():
    height = 6
    width = 7
    # Pound for empty R for red and Y for yellow
    render_board(height, width)
    player_move(width)


if __name__ == "__main__":
    # execute only if run as a script

    main()
