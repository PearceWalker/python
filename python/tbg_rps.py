#1) create a derivative class from Player

#2) create a derivative class from TurnBasedGame

        #a) With your derivative of Player as the player_class

        #b) Override the play_round() method to play a new game

from turnbased import Player, TurnBasedGame

import random 

class RpsPlayer(Player):
    def __init__(self, number):
        Player.__init__(self, number)



class RpsGame(TurnBasedGame):
    player_class = RpsPlayer

    def get_players(self):
        while self.player_type == '':
            self.player_type = input('Would you like to play a computer or a friend? (C/F)\n').upper()
            if self.player_type not in 'CF':
                print('Please enter a valid character!')
                self.player_type = ''
            else:
                self.player_type = self.player_type



    def play_round(self):
        if self.player_type == 'C':
            while not self.winner:
                player_input = input('Pick Rock, Paper, or Scissors (R/P/S)\n').upper()
                comp_sel = random.choice("RPS")
                if player_input in 'RPS':
                    if player_input == comp_sel:
                        print('You threw the same thing!')
                    elif player_input == "P" and comp_sel == "R" or player_input == "R" and comp_sel == "S" or player_input == "S" and comp_sel == "P":
                        self.winner = 'you!'
                    else:
                        self.winner = 'the computer'
                    print(f'You threw {player_input}. The computer threw {comp_sel}.')
                    
                else:
                    print('Please choose a valid play')
        if self.player_type == 'F':
            self.player1 = input('Please enter a name for player 1\n')
            self.player2 = input('Please enter a name for player 2\n')
            while not self.winner:
                print(f'It\'s time for {self.player1} to pick!\nTurn the computer away so {self.player2} can\'t see! ')
                player1_input = input('Pick Rock, Paper, or Scissors (R/P/S)\n').upper()
                '''Lots of '*' will print as to not show player1's pick'''
                veil = '*\n'
                print(veil * 100)
                print(f'Okay! {self.player2}\'s turn!')
                player2_input = input('Pick Rock, Paper, or Scissors (R/P/S)\n').upper()
                if player1_input and player2_input in 'RPS':
                    if player1_input == player2_input:
                        print('It\'s a tie!')
                    elif player1_input == "P" and player2_input == "R" or player1_input == "R" and player2_input == "S" or player1_input == "S" and player2_input == "P":
                        self.winner = self.player1
                    else:
                        self.winner = self.player2
                    if player1_input == 'R':
                        player1_input = 'Rock'
                    if player1_input == 'P':
                        player1_input = 'Paper'
                    if player1_input == 'S':
                        player1_input = 'Scissors'
                    if player2_input == 'R':
                        player2_input = 'Rock'
                    if player2_input == 'P':
                        player2_input = 'Paper'
                    if player2_input == 'S':
                        player2_input = 'Scissors'
                    print(f'{self.player1} threw {player1_input}. {self.player2} threw {player2_input}')

                else: 
                    ('One of you didn\'t enter the correct syntax. Try again!')
            
        
    

if __name__ == "__main__":
    game = RpsGame()
    game.run()