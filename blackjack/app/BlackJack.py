from .Game import Game


class BlackJack:


    def __init__(self, game):
        self.game = game
    
    def deal(self):
        self.game.get_current_state().start_game()
        if self.game.player.has_black_jack():
            self.game.get_current_state().end_player_turn()
        else:
            print("Player's turn!")

    def hit(self):
        if(type(self.game.get_current_state()) is type(self.game.get_player_turn_state())):
            self.game.draw_card_and_give_to_player()
        elif(type(self.game.get_current_state()) is type(self.game.get_dealer_turn_state())):
            self.game.draw_card_and_give_to_dealer()

    
    def stand(self):
        if(type(self.game.get_current_state()) is type(self.game.get_player_turn_state())):
            self.game.get_current_state().end_player_turn()

    
    def reset(self):
        self.game.get_current_state().reset_game()


