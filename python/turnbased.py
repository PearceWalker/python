import random

class Player:
    '''The base class for a player in TurnBasedGame'''
    def __init__(self, player_num):
        self.name = input(f"What is the name of player {player_num}? ")

    def reset(self):
        '''Run to reset a player to start a new round of the game'''

class TurnBasedGame:
    '''Base class for a turn based game'''
    player = Player
    def __init__(self, players: list = None):
        self.winner = None
        self.players = []
        self.minimum_players = 2
        self.maximum_players = 10

        if players:
            self.players = players
        else:
            self.get_players()

    def get_players(self):
        '''Menu to add players to a game'''
        add_player = "y"
        count = 1
        while add_player == "y":
            self.players.append(self.player(count))
            count += 1
            if self.maximum_players >= count > self.minimum_players:
                add_player = input("Add another player (y/n)? ").lower()
            elif self.maximum_players < count:
                add_player = "n"

    def start(self):
        '''Run at the beginning of every round'''
        self.winner = None

        for player in self.players:
            player.reset()

    def play_round(self):
        '''Play a round of the game'''
        self.winner = random.choice(self.players)

    def check_finish(self):
        '''Check the win condition (return True if the game is over)
        Override this class to look for a winner at the end of a round
        '''
        if self.winner:
            return True

    def display_results(self):
        '''Print the results of the game'''
        print(f"The winner is {self.winner.name}")

    def run(self):
        '''The main game loop for a turn based game'''
        play_again = True
        while play_again:
            self.start()
            while not self.check_finish():
                self.play_round()
            self.display_results()
            play_again = True if input("Play again (y)? ").lower() in "y\n" else False


if __name__ == "__main__":
    game = TurnBasedGame()
    game.run()