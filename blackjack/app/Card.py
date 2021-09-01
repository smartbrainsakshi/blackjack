class Card:	
	
    def __init__(self, suit, face_value):
        self._suit = suit
        self._face_value = face_value
        self._face_down = False

    def get_face_value(self):
        return self._face_value

    def is_face_down(self):
        return self._face_down

    def flip_card_face_down(self):
        self._face_down = True

    def flip_card_face_up(self):
        self._face_down = False