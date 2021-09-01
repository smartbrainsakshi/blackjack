from ..Deck import DeckSingleton

class TestDeckSingleton:

    def test_shuffle(self):
        deck = DeckSingleton().get_instance()
        deck.shuffle()
        
        pre_shuffle = next(deck)
        deck.shuffle()
        post_shuffle = next(deck)
        assert pre_shuffle != post_shuffle
    
    def test_iterator(self):
        deck = DeckSingleton().get_instance()
        cards = []

        for card in deck:
            cards.append(card)
        assert len(cards) == 52
