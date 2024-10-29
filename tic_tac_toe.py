import random

def generateMagicSquare():
    """Generates a 3x3 magic square."""
    magicSquare = [[0 for _ in range(3)] for _ in range(3)]
    i, j = 0, 1
    num = 1
    while num <= 9:
        magicSquare[i][j] = num
        next_i, next_j = (i - 1) % 3, (j + 1) % 3
        if magicSquare[next_i][next_j] != 0:
            next_i, next_j = (i + 1) % 3, j
        i, j = next_i, next_j
        num += 1
    return magicSquare

def printBoard(magicSquare, player_moves, computer_moves, player_symbol, computer_symbol):
    """Prints the board with player and computer moves."""
    print("Board:")
    for row in magicSquare:
        print(' | '.join(
            f'{player_symbol}' if num in player_moves else
            f'{computer_symbol}' if num in computer_moves else
            f'{num}'
            for num in row
        ))
        print('-' * 9)

def checkWin(magicSquare, moves):
    """Checks if the current set of moves has a winning condition."""
    magic_constant = 15
    # Check rows
    for row in magicSquare:
        if sum(num for num in row if num in moves) == magic_constant:
            return True
    # Check columns
    for col in range(3):
        if sum(magicSquare[row][col] for row in range(3) if magicSquare[row][col] in moves) == magic_constant:
            return True
    # Check diagonals
    if sum(magicSquare[i][i] for i in range(3) if magicSquare[i][i] in moves) == magic_constant:
        return True
    if sum(magicSquare[i][2 - i] for i in range(3) if magicSquare[i][2 - i] in moves) == magic_constant:
        return True
    return False

def findWinningMove(magicSquare, moves, available_numbers):
    """Finds a winning move for the given player."""
    for number in available_numbers:
        temp_moves = moves + [number]
        if checkWin(magicSquare, temp_moves):
            return number
    return None

def tossForFirstPlayer():
    """Simulates a coin toss to decide who goes first."""
    return random.choice([0, 1])

def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == "exit":
            print("Exiting the program.")
            exit()
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['yes', 'no']:
            return user_input
        else:
            print("Please enter 'yes' or 'no'.")

def playGame(magicSquare):
    """Handles the gameplay between player and computer."""
    available_numbers = [num for row in magicSquare for num in row]
    player_moves = []
    computer_moves = []

    printBoard(magicSquare, player_moves, computer_moves, " ", " ")

    human_choice = get_integer_input('Select "0" or "1" for the toss: ')
    toss_result = tossForFirstPlayer()
    if human_choice == toss_result:
        print("Human won the toss!!")
        player_symbol = 'X'
        computer_symbol = 'O'
        current_player = 'X'
    else:
        print("Computer won the toss!!")
        player_symbol = 'O'
        computer_symbol = 'X'
        current_player = 'X' 

    for turn in range(9):
        if current_player == 'X':
            if computer_symbol == 'X':
                winning_move = findWinningMove(magicSquare, computer_moves, available_numbers)
                if winning_move is not None:
                    computer_move = winning_move
                else:
                    blocking_move = findWinningMove(magicSquare, player_moves, available_numbers)
                    if blocking_move is not None:
                        computer_move = blocking_move
                    else:
                        computer_move = random.choice(available_numbers)
                print(f"Computer's choice: {computer_move}")
                computer_moves.append(computer_move)
                available_numbers.remove(computer_move)
            else:
                while True:
                    player_move = get_integer_input("Select number from the board: ")
                    if player_move not in available_numbers:
                        print("Invalid choice. Choose from the available numbers.")
                    else:
                        break
                player_moves.append(player_move)
                available_numbers.remove(player_move)
            current_player = 'O'
        else:
            if player_symbol == 'O':
                while True:
                    player_move = get_integer_input("Select number from the board: ")
                    if player_move not in available_numbers:
                        print("Invalid choice. Choose from the available numbers.")
                    else:
                        break
                player_moves.append(player_move)
                available_numbers.remove(player_move)
            else:
                winning_move = findWinningMove(magicSquare, computer_moves, available_numbers)
                if winning_move is not None:
                    computer_move = winning_move
                else:
                    blocking_move = findWinningMove(magicSquare, player_moves, available_numbers)
                    if blocking_move is not None:
                        computer_move = blocking_move
                    else:
                        computer_move = random.choice(available_numbers)
                print(f"Computer's choice: {computer_move}")
                computer_moves.append(computer_move)
                available_numbers.remove(computer_move)
            current_player = 'X'

        printBoard(magicSquare, player_moves, computer_moves, player_symbol, computer_symbol)

        if checkWin(magicSquare, computer_moves):
            print("Computer wins!")
            return
        elif checkWin(magicSquare, player_moves):
            print("Player wins!")
            return

    print("It's a draw!")

def main():
    """Main function to run the game."""
    while True:
        magicSquare = generateMagicSquare()
        playGame(magicSquare)
        play_again = get_yes_no_input("Would you like to play again? (yes/no): ")
        if play_again != 'yes':
            print("Thanks for playing!")
            break

main()
