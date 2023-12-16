import random

class Game:
    CHOICES = ["rock", "paper", "scissors"]

    def __init__(self, player_name, rounds):
        # Initialize the Game object with player name, number of rounds, and choice
        self.player_name = player_name
        self.rounds = rounds
        self.choice = None

    def get_player(self):
        # Get the player's name
        return self.player_name

    def get_rounds_num(self):
        # Get the number of rounds
        return self.rounds

    def get_choices(self, choice):
        # Get the player's choice and generate a random choice for the computer
        choice = choice.lower()
        if choice in self.CHOICES:
            self.choice = choice
            self.computer = random.choice(self.CHOICES)
            return True
        else:
            # Display an error message if the player's choice is invalid
            print("Error: Please choose one of the three choices.")
            return False

    def get_result(self):
        # Initialize points for the player and computer
        ai_points = 0
        player_points = 0

        # Iterate through the specified number of rounds
        for r in range(self.rounds):
            # Get the player's choice for each round
            player_choice = input("Enter your choice (rock/paper/scissors): ")

            # Check if the player's choice is valid
            if self.get_choices(player_choice):
                # Determine the winner for each round and update points
                if self.computer == self.choice:
                    print("Computer's choice: ", self.computer)
                    print("Winner: Draw")
                elif (self.computer == self.CHOICES[0] and self.choice == self.CHOICES[2]) or \
                     (self.computer == self.CHOICES[1] and self.choice == self.CHOICES[0]) or \
                     (self.computer == self.CHOICES[2] and self.choice == self.CHOICES[1]):
                    print("Computer's choice: ", self.computer)
                    print("Winner: Computer")
                    ai_points += 1
                else:
                    print("Computer's choice: ", self.computer)
                    print("Winner: ", self.player_name)
                    player_points += 1

        # Display the final scores and determine the overall winner
        print()
        print("========== Scores ===========")
        print(f"{self.player_name}: {player_points}")
        print(f"Computer: {ai_points}")
        print("Winner is: ")
        if player_points > ai_points:
            print(self.player_name)
        elif ai_points > player_points:
            print("Computer")
        else:
            print("Draw")
        print("=============================")
