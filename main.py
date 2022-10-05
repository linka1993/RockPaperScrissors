import random
from colorama import Fore, Style


class Game:
    user_points = 0
    computer_points = 0
    rock = Fore.BLUE + "Rock" + Style.RESET_ALL
    paper = Fore.CYAN + "Paper" + Style.RESET_ALL
    scissors = Fore.MAGENTA + "Scissors" + Style.RESET_ALL
    lizard = Fore.LIGHTGREEN_EX + "Lizard" + Style.RESET_ALL
    spock = Fore.LIGHTRED_EX + "Spock" + Style.RESET_ALL

    def __init__(self):
        pass

    def rules(self, gamer):
        choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        computer = random.choice(choices)
        Game.computer(self, computer)
        result = ""
        gamer_choice = ""
        if gamer in ('r', 'rock', 's', 'scissors', 'p', 'paper', 'l', 'lizard', 'sp', 'spock'):
            if gamer == 'r' or gamer == 'rock':
                gamer_choice = g.rock
                if computer == 'paper':
                    result = "lost"
                elif computer == 'rock':
                    result = "tie"
                elif computer == 'scissors':
                    result = "won"
                elif computer == 'lizard':
                    result = "lost"
                elif computer == 'spock':
                    result = "win"
            elif gamer == 'p' or gamer == 'paper':
                gamer_choice = g.paper
                if computer == 'paper':
                    result = "tie"
                elif computer == 'rock':
                    result = "won"
                elif computer == 'scissors':
                    result = "lost"
                elif computer == 'lizard':
                    result = "lost"
                elif computer == 'spock':
                    result = "win"
            elif gamer == 's' or gamer == 'scissors':
                gamer_choice = g.scissors
                if computer == 'paper':
                    result = "won"
                elif computer == 'rock':
                    result = "lost"
                elif computer == 'scissors':
                    result = "tie"
                elif computer == 'lizard':
                    result = "win"
                elif computer == 'spock':
                    result = "lost"
            elif gamer == 'l' or gamer == 'lizard':
                gamer_choice = g.lizard
                if computer == 'paper':
                    result = "won"
                elif computer == 'rock':
                    result = "lost"
                elif computer == 'scissors':
                    result = "lost"
                elif computer == 'lizard':
                    result = "tie"
                elif computer == 'spock':
                    result = "win"
            elif gamer == 'sp' or gamer == 'spock':
                gamer_choice = g.spock
                if computer == 'paper':
                    result = "lost"
                elif computer == 'rock':
                    result = "win"
                elif computer == 'scissors':
                    result = "win"
                elif computer == 'lizard':
                    result = "lost"
                elif computer == 'spock':
                    result = "tie"
            print(f'You picked {gamer_choice}')
            Game.reason_of_result(self, computer, gamer)
            Game.results(self, result)
        else:
            print(Fore.RED + 30*"~" + "\nThere's no weapon like that!\n" + 30*"~" + Style.RESET_ALL)

    def computer(self, computer):
        computer_choice = ""
        if computer == "rock":
            computer_choice = g.rock
        elif computer == "paper":
            computer_choice = g.paper
        elif computer == "scissors":
            computer_choice = g.scissors
        elif computer == "lizard":
            computer_choice = g.lizard
        elif computer == "spock":
            computer_choice = g.spock
        print(20*"~")
        print(f"Computer picked {computer_choice}")

    def results(self, result):
        print(Style.RESET_ALL + 20*"~")
        if result == "won":
            Game.user_points += 2
            print(Fore.GREEN + "YOU WON!!! \nCONGRATULATIONS!!")
        elif result == "tie":
            Game.user_points += 1
            Game.computer_points += 1
            print(Fore.YELLOW + "It's a tie!")
        elif result == "lost":
            Game.computer_points += 2
            print(Fore.RED + "You've lost!\nSorry ;(")
        print(Style.RESET_ALL + 20*"~")
        return Game.computer_points, Game.user_points

    def reason_of_result(self, computer, gamer):
        if (computer == "paper" and gamer in ('s', 'scissors')) or (computer == "scissors" and gamer in ('p', 'paper')):
            print(f"{g.scissors} cuts {g.paper}")
        elif (computer == "paper" and gamer in ('r', 'rock')) or (computer == "rock" and gamer in ('p', 'paper')):
            print(f"{g.paper} covers {g.rock}")
        elif (computer == "scissors" and gamer in ('r', 'rock')) or (computer == "rock" and gamer in ('s', 'scissors')):
            print(f"{g.rock} crushes {g.scissors}")
        elif (computer == "scissors" and gamer in ('sp', 'spock')) \
                or (computer == "spock" and gamer in ('s', 'scissors')):
            print(f"{g.spock} smashes {g.scissors}")
        elif (computer == "scissors" and gamer in ('l', 'lizard')) \
                or (computer == "lizard" and gamer in ('s', 'scissors')):
            print(f"{g.scissors} decapitates {g.lizard}")
        elif (computer == "paper" and gamer in ('l', 'lizard')) or (computer == "lizard" and gamer in ('p', 'paper')):
            print(f"{g.lizard} eats {g.paper}")
        elif (computer == "paper" and gamer in ('sp', 'spock')) or (computer == "spock" and gamer in ('p', 'paper')):
            print(f"{g.paper} disproves {g.spock}")
        elif (computer == "rock" and gamer in ('sp', 'spock')) or (computer == "spock" and gamer in ('r', 'rock')):
            print(f"{g.spock} vaporizes {g.rock}")
        elif (computer == "rock" and gamer in ('l', 'lizard')) or (computer == "lizard" and gamer in ('r', 'rock')):
            print(f"{g.rock} crushes {g.lizard}")
        elif (computer == "spock" and gamer in ('l', 'lizard')) or (computer == "lizard" and gamer in ('sp', 'spock')):
            print(f"{g.lizard} poisons {g.spock}")

    def play(self):
        gamer = input(Style.RESET_ALL + "What's your weapon?: ")
        gamer = gamer.lower()
        Game.rules(self, gamer)


if __name__ == '__main__':
    print(Style.RESET_ALL + "Welcome in Rock Paper Scissors game!")
    name = ""
    while not name:
        name = input("Enter your name: ")
    while True:
        print(f"\t Pick your weapon {name}:")
        print(Fore.BLUE + "\t r - Rock")
        print(Fore.CYAN + "\t p - Paper")
        print(Fore.MAGENTA + "\t s - Scissors")
        print(Fore.LIGHTGREEN_EX + "\t l - Lizard")
        print(Fore.LIGHTRED_EX + "\t sp - Spock")
        g = Game()
        g.play()
        while True:
            answer = input(Style.RESET_ALL + f"Do you want to play again {name}? (y/n): ")
            answer = answer.lower()
            if answer in ('y', 'n', 'yes', 'no'):
                break
            print(Fore.RED + "Invalid answer!")
        if answer == 'y' or answer == 'yes':
            print(20*"~")
            continue
        else:
            print(20*"~" + f'\nSCORE: \n# {name}: {g.user_points}\n# Computer: {g.computer_points}')
            print(Fore.GREEN + "GOODBYE!")
            break

