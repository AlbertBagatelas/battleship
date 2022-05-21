"""

Welcome message and infor for the player.
And sperator variable to separate the game and the information.

"""
welcome_messsage = "Welcome to Battleships Commander!"
board_info = "Board = 5x5 Ships under command = 4"
board_info_two = "The boards starts from top left row: 0 col: 0"
seperator = "x"*10

#name of the player
name = str(input("Your Name Commander:"))

# The variable for the board
board = []

# To create 5 lists to act as rows
for i in range(0,5):
    board.append(["0"] *5)

# Function to put board as a stack to become a grid
def display_board(board):
    for row in board:
        # The .join makes the grid remove the list feuture to look more streamline for a game
        print(" ".join(row))

print(seperator)
print(welcome_messsage)
print(board_info)
print(board_info_two)
print(seperator)

print("Commander: " + name)
display_board(board)