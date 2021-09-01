
class Player:

    def __init__(self):
        self._card_in_hand = []

    def get_cards(self):
        return self._card_in_hand

    def add_card_to_hand(self, card):
        self._card_in_hand.append(card)

    def remove_cards_from_hand(self):
        self._card_in_hand = []
	
    def get_hand_value(self):

        number_of_aces = 0
        hand_value = 0
        
        for c in self._card_in_hand:
            face_value = c.get_face_value()
            if "A" in face_value:
                number_of_aces+=1
            elif "2" in face_value:
                hand_value += 2
            elif "3" in face_value:
                hand_value += 3
            elif "4" in face_value:
                hand_value += 4
            elif "5" in face_value:
                hand_value += 5
            elif "6" in face_value:
                hand_value += 6
            elif "7" in face_value:
                hand_value += 7
            elif "8" in face_value:
                hand_value += 8
            elif "9" in face_value:
                hand_value += 9
            elif "10" in face_value:
                hand_value += 10
            elif "J" in face_value:
                hand_value += 10
            elif "Q" in face_value:
                hand_value += 10
            elif "K" in face_value:
                hand_value += 10
        

        for i in range(number_of_aces):
            if hand_value + 11 > 21:
                hand_value += 1
            else:
                hand_value += 11		
        return hand_value

    def has_busted_hand(self):
        return self.get_hand_value() > 21

    def has_black_jack(self):
        return self.get_hand_value() == 21

    def show_cards(self):
        res = ""
        for each in self._card_in_hand:
            if each.is_face_down():
                res+=" ?"
            else:
                res+=f" {each.get_face_value()}"
        return res

    def show_all_cards(self):    
        for each in self._card_in_hand:
            print(each.get_face_value(), " ")


