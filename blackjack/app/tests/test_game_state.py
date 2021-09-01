from ..Game import Game

class TestGameState:

    def test_init_state(self):
        game = Game()
        assert type(game.current_state) == type(game.start_state)

    def test_set_state(self):
        game = Game()
        game.set_state(game.get_player_turn_state())
        assert type(game.current_state) == type(game.player_turn_state)

    def test_start_state(self):
        game = Game()
        game.set_state(game.get_start_state())

        game.get_current_state().end_player_turn()
        assert type(game.get_current_state()) == type(game.get_start_state())

        game.get_current_state().end_round()
        assert type(game.get_current_state()) == type(game.get_start_state())

        game.get_current_state().start_game()
        assert type(game.get_current_state()) == type(game.get_player_turn_state())

    def test_player_turn_state(self):
        game = Game()
        game.set_state(game.get_player_turn_state())

        game.get_current_state().start_game()
        assert type(game.get_current_state()) == type(game.get_player_turn_state())


    def test_dealer_turn_state(self):
        game = Game()
        game.set_state(game.get_dealer_turn_state())
        
        game.get_current_state().end_player_turn()
        assert type(game.get_current_state()) == type(game.get_dealer_turn_state())

        
        game.get_current_state().start_game()
        assert type(game.get_current_state()) == type(game.get_dealer_turn_state())
        
        game.get_current_state().end_round()
        assert type(game.get_current_state()) == type(game.get_round_end_state())	



    def test_round_end_state(self):
        game = Game()
        game.set_state(game.get_round_end_state())
        
        game.get_current_state().end_player_turn()
        assert type(game.get_current_state()) == type(game.get_round_end_state())
        
        game.get_current_state().end_round()
        assert type(game.get_current_state()) == type(game.get_round_end_state())
        
        game.get_current_state().start_game()
        assert type(game.get_current_state()) == type(game.get_round_end_state())

