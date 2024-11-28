def print_hexagon(size):
    # Print the top half of the hexagon
    for i in range(size):
        spaces = " " * (size - i - 1)
        stars = "* " * (size + i)
        print(spaces + stars)

    # Print the bottom half of the hexagon
    for i in range(size - 1, -1, -1):
        spaces = " " * (size - i - 1)
        stars = "* " * (size + i)
        print(spaces + stars)
def movement_guide():
    testboard = [(4, 4, 1)]

    print("this is the initial board:")
    print_board(testboard)

    print("after applying ** h- **")
    print_board(apply_move(testboard, "h-"))

    print("after applying ** h+ **")
    print_board(apply_move(testboard, "h+"))

    print("after applying ** d- **")
    print_board(apply_move(testboard, "d-"))

    print("after applying ** d+ **")
    print_board(apply_move(testboard, "d+"))

    print("after applying ** a- **")
    print_board(apply_move(testboard, "a-"))

    print("after applying ** a+ **")
    print_board(apply_move(testboard, "a+"))
    
    
def is_board_point(a, b):
    c = a - b
    if (0 <= a and a <= 8
        and
        0 <= b and b <= 8
        and
        -4 <= c and c <= 4):
        return True
    return False
def print_board_basic():
    for i in range(8, 4, -1):
        print(" " * (i - 4), end = "")
        for j in range(i-4, 9):
            print(str(chr(ord('a')+i))+str(j), end = "")
        print()
    for i in range(4, -1, -1):
        print(" " * (4 - i), end="")
        for j in range(5 + i):
            print(str(chr(ord('a')+i))+str(j), end = "")
        print()
    
def print_board(board):
    for i in range(8, 4, -1):
        print(" " * (i - 4), end = "")
        for j in range(i-4, 9):
            if (i, j, 0) in board:
                print("* ", end = "")
            elif (i, j, 1) in board:
                print("- ", end = "")
            else:
                print("O ", end = "")
        print() 
    for i in range(4, -1, -1):
        print(" " * (4 - i), end="")
        for j in range(5 + i):
            if (i, j, 0) in board:
                print("* ", end = "")
            elif (i, j, 1) in board:
                print("- ", end = "")
            else:
                print("O ", end = "")
        print()
              
#
def apply_move(tekkeha, move):
    if len(move)!= 2:
        print(f'an error occured in apply_move func with params: tekkeha = {tekkeha} and move = {move}')
    ax = move[0]
    direction = move[1]
    newtekkeha = []
    if ax == 'h':
        if direction == '-':
            for tekke in tekkeha:
                newtekkeha.append((tekke[0], tekke[1] - 1, tekke[2]))
        elif direction == '+':
            for tekke in tekkeha:
                newtekkeha.append((tekke[0], tekke[1] + 1, tekke[2]))
        else:
            print(f'please enter a valid direction, either - or +, not {direction}')
    elif ax == 'a':
        if direction == '-':
            for tekke in tekkeha:
                newtekkeha.append((tekke[0] - 1, tekke[1], tekke[2]))
        elif direction == '+':
            for tekke in tekkeha:
                newtekkeha.append((tekke[0] + 1, tekke[1], tekke[2]))
        else:
            print(f'please enter a valid direction, either - or +, not {direction}')
    elif ax == 'd':
        if direction == '-':
            for tekke in tekkeha:
                newtekkeha.append((tekke[0] - 1, tekke[1] - 1, tekke[2]))
        elif direction == '+':
            for tekke in tekkeha:
                newtekkeha.append((tekke[0] + 1, tekke[1] + 1, tekke[2]))
        else:
            print(f'please enter a valid direction, either - or +, not {direction}')
    else:
        print(f'please enter a valid axis, either h or d or a, not {ax}')


    return newtekkeha









def apply_move2(board, move, player):
    if len(move) == 4:
        tekke = move[0:2]
        bordar = move[2:4]
        moved_tekkeha = apply_move_helper
    elif len(move) == 6:
        pass
    elif len(move) == 8:
        pass
    else:
        print("maskhare kardi?")
## each tekke is shown in the format of (sefid, qermez, player \in {0, 1})
board = [(0, 0, 0), (0, 1, 0), (0, 2, 0), (0, 3, 0), (0, 4, 0),
         (1, 0, 0), (1, 1, 0), (1, 2, 0), (1, 3, 0), (1, 4, 0), (1, 5, 0),
         (2, 2, 0), (2, 3, 0), (2, 4, 0)]
board2= [(8, 8, 1), (8, 7, 1), (8, 6, 1), (8, 5, 1), (8, 4, 1),
         (7, 8, 1), (7, 7, 1), (7, 6, 1), (7, 5, 1), (7, 4, 1), (7, 3, 1),
         (6, 6, 1), (6, 5, 1), (6, 4, 1)]

board.extend(board2)


















