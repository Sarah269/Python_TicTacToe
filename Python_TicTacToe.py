#Cisco Networking Academy Python Essentials 1
#Final Project:  TicTacToe
#
#Begin function definitions


def display_board(board):
  # The function accepts one parameter containing the     # board's current status
  # and prints it out to the console.

  for i in range(3):
    print(" +-------+-------+-------+")
    print(" |       |       |       |")
    for j in range(3):
      if j == 2:
        print(" |  ", board[i][j], "  |", end="")
      else:
        print(" |  ", board[i][j], " ", end="")
    print("\n", "|       |       |       |")
  print(" +-------+-------+-------+")


def make_list_of_free_fields(board):
  #The function browses the board and builds a list of all the
  #free squares; the list consists of tuples, while each tuple
  #is a pair of row and column numbers. Function returns
  #a dictionary with free square indices and square number
  #initialize list and dictionary
  #build the dictionary of free squares
  #keys:  square number, values: board square tuples

  #Initialize the dictionary
  #list is not used
  free_sq = []
  freesq_dict = {}
  for i in range(3):
    for j in range(3):
      if board[i][j] in range(1, 10):
        free_sq.append((i, j))
        freesq_dict[board[i][j]] = i, j
  return freesq_dict


def moves_left(board):
  #The function checks if there are any moves leftmoves_left(board):

  #Initialize dictionary
  freesquares = {}
  freesquares = make_list_of_free_fields(board)
  if freesquares == {}:
    return False
  else:
    return True


def draw_move(board):
  #The function draws the computer's move and updates the board.
  #Computer's symbol is 'X'

  #import random function
  import random

  #Initialize
  get_move = True
  availsq_dict = {}
  availsq_dict = make_list_of_free_fields(board)

  while get_move:
    computer_move = random.randint(1, 9)
    if computer_move in availsq_dict.keys():
      a, b = availsq_dict[computer_move]
      #print(a,b)
      #print(computer_move)
      #update board
      board[a][b] = 'X'
      get_move = False


def enter_move(board):
  #The function accepts the board's current status, asks the user about
  #their move, checks the input, and
  #updates the board according to the user's decision.

  #Initialize
  select_move = True
  freecell_dict = {}
  freecell_dict = make_list_of_free_fields(board)

  #Get the computer's move and update the board

  while select_move:
    try:
      move = int(input("Enter Your Move: "))
      if move in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if move in freecell_dict.keys():
          a, b = freecell_dict[move]
          #print(a,b)
          board[a][b] = 'O'
          select_move = False
        else:
          print("Cell is not free.  Try again")
      else:
        print("Enter a value from 1 to 9")

    except ValueError:
      print("value error")
    except:
      print("Incorrect value.  Enter a value from 1 to 9")


def victory_for(board, sign):
  #The function analyzes the board's status in order to
  #check if the payer using 'O's or 'X's has won the game

  #Check rows for a winner
  if (board[0].count(sign) == 3) or (board[1].count(sign)
                                     == 3) or (board[2].count(sign) == 3):
    #print("Rows: ","you won")
    print(sign, " Won!")
    return True
  #Check columns for a winner
  elif (board[0][0], board[1][0], board[2][0]).count(sign) == 3:
    #print("col1: ", "you won")
    print(sign, " Won!")
    return True
  elif (board[0][1], board[1][1], board[2][1]).count(sign) == 3:
    #print("col2: ", "you won")
    print(sign, " Won!")
    return True
  elif (board[0][2], board[1][2], board[2][2]).count(sign) == 3:
    #print("col3: ", "you won")
    print(sign, " Won!")
    return True

  #Check diagonal Left_to_Right
  elif (board[0][0], board[1][1], board[2][2]).count(sign) == 3:
    #print("Diagonal L_to_R: ", "you won")
    print(sign, " Won!")
    return True
  #Check diagonal Right_to_Right
  elif (board[0][2], board[1][1], board[2][0]).count(sign) == 3:
    #print("Diagonal R_to_L: ", "you won")
    print(sign, " Won!")
    return True
  else:
    #print("No winner")
    return False


#End of function definitions

#Initialize tictactoe board
tictactoe = []
tictactoe = [[0 for i in range(3)] for j in range(3)]
tictactoe[0] = [1, 2, 3]
tictactoe[1] = [4, 5, 6]
tictactoe[2] = [7, 8, 9]

#Start Game
#First move belongs to the computer
#Computer will place an 'X' in the middle of the board, box 5

tictactoe[1][1] = "X"

game_over = False

while not game_over:
  if moves_left(tictactoe):
    display_board(tictactoe)
    enter_move(tictactoe)
    if victory_for(tictactoe, 'O'):
      display_board(tictactoe)
      game_over = True
  else:
    display_board(tictactoe)
    if not victory_for(tictactoe, 'O'):
      print("Draw.  No winner")
    game_over = True

  if game_over != True:
    if moves_left(tictactoe):
      display_board(tictactoe)
      draw_move(tictactoe)
      if victory_for(tictactoe, 'X'):
        display_board(tictactoe)
        game_over = True
    else:
      display_board(tictactoe)
      if not victory_for(tictactoe, 'X'):
        print("Draw. No winner")
      game_over = True
