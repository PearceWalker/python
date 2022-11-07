from turnbased import Player, TurnBasedGame

class RpsPlayer(Player):
    def __init__(self, number):
        Player.__init__(self, number)




class RpsGame(TurnBasedGame):
    player = RpsPlayer

    


if __name__ == "__main__":
    game = RpsGame()
    game.run()