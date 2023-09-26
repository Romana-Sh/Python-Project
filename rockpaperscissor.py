import random


class RockPaperScissors:

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.options = {'rock': 0, 'paper': 1, 'scissors': 2}

    def random_choice(self):

        return random.choice(list(self.options.keys()))

    def check_win(self, player, opponent):

        result = (player - opponent) % 3
        if result == 0:
            self.ties += 1
            print("The game is a tie!")
        elif result == 1:
            self.wins += 1
            print("You win!")
        elif result == 2:
            self.losses += 1
            print("I Win")

    def print_score(self):
        print(f"You have {self.wins} wins, {self.losses} losses, and "
              f"{self.ties} ties.")

    def run_game(self):
        while True:
            userchoice = input("Choices are 'rock', 'paper', or 'scissors'.\n"
                               "Which one do you choose? ").lower()
            if userchoice not in self.options.keys():
                print("Invalid input, try again!")
            else:
                break
        opponent_choice = self.random_choice()
        print(f"You've picked {userchoice}, and I picked {opponent_choice}.")
        self.check_win(self.options[userchoice], self.options[opponent_choice])


if __name__ == "__main__":
    game = RockPaperScissors()
    while True:
        game.run_game()
        game.print_score()

        while True:

            continue_prompt = input(
                '\nDo you wish to play again? (y/n): ').lower()
            if continue_prompt == 'n':
                print("Good Bye!")
                exit()
            elif continue_prompt == 'y':
                break
            else:
                print("Invalid input!\n")
                continue
