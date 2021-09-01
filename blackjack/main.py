
import app

class Handler:
    def __init__(self):
        self.game = app.Game()
        self.blackjack = app.BlackJack(self.game)
    
    def run(self):
        self.game.play(self.blackjack)




if __name__ == '__main__':
    handler = Handler()
    handler.run()

