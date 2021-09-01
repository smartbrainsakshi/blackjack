from abc import ABC, abstractmethod
class IGameState(ABC):
    """
    State Design Pattern
    """

    @abstractmethod
    def start_game(self):
        pass

    @abstractmethod
    def end_player_turn(self):
        pass
    
    @abstractmethod
    def end_round(self):
        pass

    @abstractmethod
    def reset_game(self):
        pass


class PlayerTurnState(IGameState):

    def __init__(self, game):
        self.game = game

    def start_game(self):
        return

    def end_player_turn(self):
        self.game.flip_dealer_cards_face_up()
        self.game.set_state(self.game.get_dealer_turn_state())

    def end_round(self):
        self.game.set_state(self.game.get_round_end_state())

    def reset_game(self):
        return

class RoundEndState(IGameState):

    def __init__(self, game):
        self.game = game

    def start_game(self):
        return

    def end_player_turn(self):
        return

    def end_round(self):
        return

    def reset_game(self):
        self.game.reset()
        self.game.set_state(self.game.get_start_state())

class DealerTurnState(IGameState):

    def __init__(self, game):
        self.game = game

    def start_game(self):
        return

    def end_player_turn(self):
        return

    def end_round(self):
        self.game.set_state(self.game.get_round_end_state())

    def reset_game(self):
        return


class StartState(IGameState):

    def __init__(self, game):
        self.game = game

    def start_game(self):
        self.game.deal_cards()
        self.game.set_state(self.game.get_player_turn_state())

    def end_player_turn(self):
        return

    def end_round(self):
        return

    def reset_game(self):
        return