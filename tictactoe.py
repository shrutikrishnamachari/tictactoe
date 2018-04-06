def twoplayer():

    win = False

    def printboard():
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('-----------')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('-----------')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    board = ["0","1","2","3","4","5","6","7","8","9"]
    print("Note the name of each spot carefully!")
    printboard()

    board = [" "," "," "," "," "," "," "," "," "," "]

    def player_1_move():
        move_number = input("Player One Choose a Spot from 1 - 9!")
        if board[int(move_number)] == " ":
            board[int(move_number)] = "O"
            printboard()
        else:
            print("This spot is taken! You have lost a turn!")

    def player_2_move():
        move_number = input("Player Two Choose a Spot from 1 - 9!")
        if board[int(move_number)] == " ":
            board[int(move_number)] = "X"
            printboard()
        else:
            print("This spot is taken! You have lost a turn!")

    def check_win(player):
        global win
        if board[1]==player and board[2]==player and board[3]== player:
            print( player + " WIN")
            win = True
        elif board[4]==player and board[5]==player and board[6]== player:
            print( player + " WIN")
            win = True
        elif board[7]==player and board[8]==player and board[9]== player:
            print( player + " WIN")
            win = True
        elif board[1]==player and board[4]==player and board[7]== player:
            print( player + " WIN")
            win = True
        elif board[2]==player and board[5]==player and board[8]== player:
            print( player + " WIN")
            win = True
        elif board[3]==player and board[6]==player and board[9]== player:
            print( player + " WIN")
            win = True
        elif board[1]==player and board[5]==player and board[9]== player:
            print( player + " WIN")
            win = True
        elif board[3]==player and board[5]==player and board[7]== player:
            print( player + " WIN")
            win = True


    while win == False:
        player_1_move()
        check_win("O")
        if win == False:
            player_2_move()
            check_win("X")

def one_player():
    player_1 = "O"
    player_2 = "X"
    winn = False
    import random

    def printboard():
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('-----------')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('-----------')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print("Note the name of each spot carefully!")
    printboard()

    board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def player_1_move():
        move_number = input("Player One Choose a Spot from 1 - 9!")
        if board[int(move_number)] == " ":
            board[int(move_number)] = "O"
            printboard()
        else:
            print("This spot is taken! You have lost a turn!")

    def player_2_move():
        move_number = random.randint(1, 9)
        if board[int(move_number)] == " ":
            board[int(move_number)] = "X"
            printboard()
        else:
            player_2_move(i)

    def check_win(player):
        global winn
        if board[1] == player and board[2] == player and board[3] == player:
            print(player + " WIN")
            winn = True
        elif board[4] == player and board[5] == player and board[6] == player:
            print(player + " WIN")
            winn = True
        elif board[7] == player and board[8] == player and board[9] == player:
            print(player + " WIN")
            winn = True
        elif board[1] == player and board[4] == player and board[7] == player:
            print(player + " WIN")
            winn = True
        elif board[2] == player and board[5] == player and board[8] == player:
            print(player + " WIN")
            winn = True
        elif board[3] == player and board[6] == player and board[9] == player:
            print(player + " WIN")
            winn = True
        elif board[1] == player and board[5] == player and board[9] == player:
            print(player + " WIN")
            winn = True
        elif board[3] == player and board[5] == player and board[7] == player:
            print(player + " WIN")
            winn = True


    while winn == False:
        player_1_move()
        check_win("O")
        if win == False:
            player_2_move()
            check_win("X")


game_type = input("How many players: 1 or 2?")
if game_type == '1':
    one_player()
elif game_type == '2':
    twoplayer()