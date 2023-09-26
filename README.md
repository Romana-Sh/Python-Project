# Projects Python Rock, Paper, Scissor game

Introduction:
Rock, Paper, or Scissors is game where two users use their hands to show if its rock or paper or scissors and reveal at the same time. The winners are determined by following rules:
1. Rock blunts Scissors (Rock wins over Scissors)
2. Scissors cut paper (Scissor wins over paper)
3. Paper covers Rock (Paper wins over Rock)
4. A tie - if both players choose the same option, players play another round
to break the tie.
Design and Implementation:
Initiate a class to handle an instance of a Rock, Paper, Scissors game with unlimited rounds. Then initiate variables.

class RockPaperScissors:
   def __init__(self):
       self.wins = 0
       self.losses = 0
       self.ties = 0
       self.options = {'rock': 0, 'paper': 1, 'scissors': 2}


#Define a random function for computer to choose random options.
def random_choice(self):
      return random.choice(list(self.options.keys()))

#Define another function to check if player wins or looses. Parameter player is player choice from self.options. Parameter opponent is computer choice from self.options.
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

  #Print current score of the player.
  def print_score(self):
       print(f"You have {self.wins} wins, {self.losses} losses, and "
             f"{self.ties} ties.")
  
  #Player plays a round of game with computer.
  while True:
           userchoice = input("Choices are 'rock', 'paper', or
            'scissors'.\n"
            "Which one do you choose? ").lower()
           if userchoice not in self.options.keys():
               print("Invalid input, try again!")
           else:
              break
       opponent_choice = self.random_choice()
      print(f"You've picked {userchoice}, and I picked
{opponent_choice}.")
        self.check_win(self.options[userchoice],
        self.options[opponent_choice])
        
#Prompt user if wants to continue game or not. Print based on user choice.
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
