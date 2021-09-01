from .Player import *

class Dealer(Player):

    def __init__(self):
        super().__init__()
    
    def flip_cards_face_up(self):
        for card in self._card_in_hand:
            card.flip_card_face_up()
