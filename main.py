import roshambo_game

player_name = input("Enter your name: ")
rounds = int(input("Enter the number of rounds you want to play: "))
game = roshambo_game.Game(player_name, rounds)
game.get_result()