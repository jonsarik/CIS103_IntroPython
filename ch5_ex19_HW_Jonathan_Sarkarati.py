# Created by Jonathan Sarkarati
# 10/25/23
# Random Number Guessing Game
# This program plays a game of "getting hot or cold."
import random

# Contstants for the game
MIN = 1
MAX = 100

def main():
    print_intro()   # Program description
    magic_number = random.randint(MIN, MAX)

    # Controlling the loop
    play_again = 'y'
    while play_again == 'y' or play_again == 'Y':
        
        count = 1
        guess = int(input('\nMake a guess: '))
        while guess > magic_number:
            guess = int(input('Too high, try again: '))
            count+=1           
        while guess < magic_number:
            guess = int(input('Too low, try again: '))
            count+=1
        game_result(count)
       
        # Play another game?
        print()
        play_again = input('Play another round? (y = yes): ')
        magic_number = random.randint(MIN, MAX)
    exit_program()
        
# Explain the game
def print_intro():
    print()
    print("Let's play a game! The computer will pick a number")
    print('between 1 and 100. Can you guess the number?')

# When player guesses correctly
def game_result(count):
    print()
    print('Nicely done!')
    if count == 1:
        print(f'It took only {count} guess to find the magic number!')
    else:
        print(f'It took only {count} guesses to find the magic number!')

# End program
def exit_program():
    print()
    print('Exiting program...')
    print('Remember: The only winning move is not to play!')

if __name__ == '__main__':
    main()
