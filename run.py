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
print("Commander: " + name)
display_board(board)