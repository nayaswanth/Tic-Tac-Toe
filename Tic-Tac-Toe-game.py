board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
symbols = ['X', 'O']
count = 1
sym_bol = ''

# Display the board function


def display_board(board):
    # print(' | | ')
    print(board[1]+'|'+board[2]+'|'+board[3])
    # print(' | | ')
    print('-----')
    # print(' | | ')
    print(board[4] + '|' + board[5] + '|' + board[6])
    # print(' | | ')
    print('-----')
    # print(' | | ')
    print(board[7] + '|' + board[8] + '|' + board[9])
    # print(' | | ')
    # print(symbol)

# Take input function


def take_input():
    first_char = input('Player 1 which alphabet do you want "X" or "O" :')
    # if(char.isalpha()):
    first_char = first_char.upper()
    if first_char == 'X':
        symbols[0] = 'X'
        symbols[1] = 'O'
        return
    elif first_char == 'O':
        symbols[0] = 'O'
        symbols[1] = 'X'
        return
    else:
        print("please select X or O ")
        take_input()


# Place their input on the board function

def place_input_on_board():
    global count
    global sym_bol
    add = True
    while add:
        num = input('Enter the index number (1-9)')
        if num.isdigit():
            num = int(num)
            if 0 < num < 10:
                if board[num] == ' ':
                    if count % 2 != 0:
                        board[num] = symbols[0]
                        sym_bol = symbols[0]
                        count += 1
                        break
                    else:
                        board[num] = symbols[1]
                        sym_bol = symbols[1]
                        count += 1
                        break
                else:
                    print('Place is already occupied')
                    continue
        print('Please Enter number in range (1-9)')
        # add=False


# check the game whether it is won function

def win_detector(board, symbol):
    global sym_bol
    if count % 2 != 0:
        symbol = symbols[1]
        sym_bol = symbols[1]
    else:
        symbol = symbols[0]
        sym_bol = symbols[0]

    if((board[1] == symbol and board[2] == symbol and board[3] == symbol) or  # top across
       (board[4] == symbol and board[5] == symbol and board[6] == symbol) or  # middle across
       (board[7] == symbol and board[8] == symbol and board[9] == symbol) or  # bottom across
       (board[1] == symbol and board[4] == symbol and board[7] == symbol) or  # left down
       (board[2] == symbol and board[5] == symbol and board[8] == symbol) or  # middle down
       (board[3] == symbol and board[6] == symbol and board[9] == symbol) or  # right down
       (board[1] == symbol and board[5] == symbol and board[9] == symbol) or  # diagonal 1
       (board[7] == symbol and board[5] == symbol and board[3] == symbol)     # diagonal 2
      ):
        return True
    else:
        if count % 2 != 0:
            sym_bol = symbols[0]

        else:
            sym_bol = symbols[1]
        return False


# Ask players if they want to play function

def next_game():
    char = input('Do you want to one more game? Y/N :')
    char = char.upper()
    if char == 'Y' or char == 'N':
        return char
    else:
        print('Please enter Y or N')
        next_game()


# main instructions
want_to_play_game = True
while want_to_play_game:
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    sym_bol = ''
    take_input()                                                            # ask for input
    play_game = True
    while play_game:
        if count < 10 and not (win_detector(board, sym_bol)):
            place_input_on_board()                                          # place input on board
            display_board(board)                                            # Display board
            # print(sym_bol)
            if win_detector(board, sym_bol):
                if sym_bol == symbols[0]:
                    print('Player 1 won the game')                          # Player 1 wins
                    count = 1
                    break
                else:
                    print('Player 2 won the game')                          # Player 2 wins
                    count = 1
                    break
            play_game = True
        # print(count)
        elif count >= 10:
            count = 1
            print('Game is drawn')                                         # Game Drawn
            play_game = False
    further_game = next_game()                                             # Play next game?
    if further_game == 'Y':
        want_to_play_game = True
    else:
        want_to_play_game = False

