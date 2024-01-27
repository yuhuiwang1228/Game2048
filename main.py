import utilities
import random

def main(iters):
    game = utilities.game(4)
    game.add_new()
    game.add_new()
    game.print_board()

    for _ in range(iters):
        move = input("Enter your move (w, s, a, d): ")
        try:
            game.check_valid_input(move)
        except ValueError:
            print('Invalid input! Please enter w, s, a, or d.')
            continue
        else:
            game.play(move)
            game.add_new()
            game.print_board()
            if game.check_win():
                print("Congratulations! You've reached 2048!")
                break
            if game.is_full():
                print("Game Over!")
                break


if __name__ == "__main__":
    main(1000)
