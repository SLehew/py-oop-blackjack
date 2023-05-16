import random

TOOLS = ['rock', 'paper', 'scissors']



class Player:
    def __init__(self, name):
        self.choice = None
        self.name = name

    def __str__(self):
        return self.name


class ComputerPlayer:
    def __init__(self):
        self.choice = None

    def get_computer_tool(self, tools):
        computer_tool = random.choice(tools)
        self.choice = computer_tool


class Game:
    def __init__(self):
        self.player = Player(self.get_player_name())
        self.computer_player = ComputerPlayer()
        self.player_choice = self.choice()
        self.evaluation()
        


    def get_player_name(self):
        name = input('What is your name? ')
        return name


    def choice(self):
        choice = input('Select (R)🪨, (P)📄, (S)✂️: ')
        return choice


    def evaluation(self):
        if self.computer_player.choice == 'rock' and self.player_choice == 's':
            print('🪨 beats ✂️, You Lose')
        if self.computer_player.choice == 'paper' and self.player_choice == 's':
            print('✂️ beats 📄, You Win!')
        if self.computer_player.choice == 'scissors' and self.player_choice == 's':
            print("✂️ versus ✂️, it's a Tie")
        if self.computer_player.choice == 'rock' and self.player_choice == 'p':
            print('📄 beats 🪨, You Win!')
        if self.computer_player.choice == 'paper' and self.player_choice == 'p':
            print("📄 versus 📄, it's a Tie!")
        if self.computer_player.choice == 'scissors' and self.player_choice == 'p':
            print('✂️ versus 📄, You Lose')
        if self.computer_player.choice == 'rock' and self.player_choice == 'r':
            print("🪨 versus 🪨, it's a Tie")
        if self.computer_player.choice == 'paper' and self.player_choice == 'r':
            print('📄 versus 🪨, you Lose')
        if self.computer_player.choice == 'scissors' and self.player_choice == 'r':
            print('✂️ versus 🪨, You Win!')


    def play_again(self):
        go_again = input('Would you like to play again? Y or N?')
        if go_again == 'y':
            
                


new_game = Game()
new_game.computer_player.get_computer_tool(TOOLS)
print(new_game.evaluation())
new_game.play_again()
