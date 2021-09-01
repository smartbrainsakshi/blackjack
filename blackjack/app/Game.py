
from .GameState import StartState, PlayerTurnState, DealerTurnState, RoundEndState

from .Player import Player
from .Dealer import Dealer
from .Deck import DeckSingleton

import time
	
class Game:
	
	def __init__(self):
		self.start_state = StartState(self)
		self.player_turn_state = PlayerTurnState(self)
		self.dealer_turn_state = DealerTurnState(self)
		self.round_end_state = RoundEndState(self)
		self.current_state = self.start_state		
		self.player =  Player()
		self.dealer =  Dealer()
		self.deck = DeckSingleton().get_instance()
	
	def set_state(self, new_state):
		self.current_state = new_state
	
	def get_current_state(self):
		return self.current_state
	
	def get_start_state(self):
		return self.start_state

	def get_player_turn_state(self):
		return self.player_turn_state
	
	def get_dealer_turn_state(self):
		return self.dealer_turn_state
	
	def get_round_end_state(self): 
		return self.round_end_state

	def play(self, blackjack):
		running = True
		
		# start the deal
		blackjack.deal()

		while(running):
			
			# display dealer's
			print(f" Dealer has: {self.dealer.show_cards()} = ?")
			# display player's
			print(f" Player has: {self.player.show_cards()} = {self.player.get_hand_value()}")

			if(self.player.has_black_jack()):
				print("Player has 21!\n"+self.get_winner())
				self.current_state.end_round()
				break		
			

			print("Would you like to (H)it or (S)tand?")
			action = input()
			if action == 'H':
				blackjack.hit()
			elif action == "S":
				blackjack.stand()
				if type(self.current_state) == type(self.dealer_turn_state):
					print(f"Player stands with: {self.player.show_cards()} = {self.player.get_hand_value()}")
			else:
				print("Either (H)it or (S)tand")

			
			if(type(self.current_state) is type(self.player_turn_state)):
				if(self.player.has_busted_hand()):
					print(f"Player has: {self.player.show_cards()} = {self.player.get_hand_value()}")
					print(f"Player busts with {self.player.get_hand_value()}")
					print(f"Dealer wins")
					self.current_state.end_round()
					break
				
				
				if(self.player.has_black_jack()):
					print("Player wins!")
					print("BlackJack!")
					self.current_state.end_round()	
					break	
			
			if(type(self.current_state) is type(self.dealer_turn_state)):
				while(True):
					print(f" Dealer has: {self.dealer.show_cards()} = {self.dealer.get_hand_value()}")
					if(self.dealer_should_end_turn()):
						if(self.dealer.has_black_jack()):
							print("Dealer has Blackjack!\n"+self.get_winner())
						elif(self.dealer.has_busted_hand()):
							print("Dealer Busted!\n"+self.get_winner())
						else:
							print("Dealer stands\n")
							print("Player Wins!")
							print(f"{self.player.show_cards()} to Dealer's {self.dealer.show_cards()} = {self.dealer.get_hand_value()}")
						
						self.current_state.end_round()
						break

					
					if(not self.dealer_should_end_turn()):
						print("Dealer hits")
						self.draw_card_and_give_to_dealer(False)
						if(self.dealer.has_black_jack()):
							print("Dealer has 21!\n"+self.get_winner())
							self.current_state.end_round()
							break
						if(self.dealer.has_busted_hand()):
							print("Dealer Busts!\n"+self.get_winner())
							self.current_state.end_round()
							break
				break
			

	
	def deal_cards(self):
		for i in range(2):
			self.draw_card_and_give_to_player()
			if(i == 0):
				self.draw_card_and_give_to_dealer(False)
			else:
				self.draw_card_and_give_to_dealer(True)

	
	def draw_card_and_give_to_dealer(self, face_down):
		try:
			card = next(self.deck)
			if face_down:
				card.flip_card_face_down()
			self.dealer.add_card_to_hand(card)
		except StopIteration as e:
			print(e)
	
	def draw_card_and_give_to_player(self):
		try:
			self.player.add_card_to_hand(next(self.deck))
		except StopIteration as e:
			print(e)
	
	def shuffle_deck(self):
		self.deck.shuffle()
	
	def get_players_cards(self):
		return self.player.get_cards()
	def get_dealer_cards(self):
		return self.dealer.get_cards()

	def dealer_should_end_turn(self): 
		return (self.dealer.has_black_jack() or self.dealer.has_busted_hand() or ((self.dealer.get_hand_value() >= 17) and (self.dealer.get_hand_value() >= self.player.get_hand_value())))

	def flip_dealer_cards_face_up(self):
		self.dealer.flip_cards_face_up()
	
	def get_winner(self):
		if(self.player.has_busted_hand() and not self.dealer.has_busted_hand()):
			return "Dealer Wins!"

		elif(not self.player.has_busted_hand() and self.dealer.has_busted_hand()):
			return "Player Wins!"

		elif(self.player.get_hand_value() > self.dealer.get_hand_value()):
			return "Player Wins!"

		elif(self.player.get_hand_value() < self.dealer.get_hand_value()):
			return "Dealer Wins!"
		else:
			return "It's a tie!"








