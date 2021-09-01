from collections.abc import Iterator
import random
from .Card import Card
from .Enum import SUIT

class DeckSingleton(Iterator):
	
	def __init__(self):

		self.total_cards = 52
		self.iterator_position = 0
		self.unique_instance = None
		self.cards = []

		
		for each in SUIT:
			for i in range(2, 11):
				self.cards.append(Card(suit=each, face_value=str(i)))
			for i in ["Q", "J", "K", "A"]:
				self.cards.append(Card(suit=each, face_value=i))
		self.shuffle()
		
	def __next__(self):
		try:
			card = self.cards[self.iterator_position]
			self.iterator_position+=1
			return card
		except IndexError:
			raise StopIteration()

	def get_instance(self):
		if(self.unique_instance is None):
			self.unique_instance = DeckSingleton()
				
		return self.unique_instance
	
	
	def shuffle(self):
		random.shuffle(self.cards)
		self.iterator_position = 0



