
## Description

Command line version of single line BlackJack game.


## How to run?

Requires a python setup.


     python main.py

  

## Assumptions

In the below case: if the player gets 21 with first two cards, we will declare him winner.

Dealer has: 6 4 = ?

Player has: A K = 21

Player has 21!

Player Wins!

  

## What I did well on this project?

The problem was straight forward if done through if-else methodology and in the same flow of functional implementation.

Instead, I preferred the Object Oriented Way via Classes and Design patterns to make the code clear to understand and maintainable to add or remove functionalities.

  

## Rationale on design choices, algorithmic decisions made


Relating a problem to real life simplifies the code too. On similar lines, I visualized the game's behavior and interactions with the user.

There are different entities like Cards, Player, Dealer, Deck.

The game has different status and information contained after every move from start to end. Each of the move had its own decisions and validations. Considering the possibility of adding more logics or moves, [State Design Pattern](https://refactoring.guru/design-patterns/state/python/example#:~:text=State%20is%20a%20behavioral%20design,of%20acting%20on%20its%20own.) was appropriate.

Apart from this the Deck is a set of various cards. Thus, the deck is made an Iterable Class, to get random next card to be drawn from it.

  
## What would I improve
I would make it work for multiple game plays, insted of current exiting after one. Refactoring of the play() which handles the input and check for result.


## What manual tests I ran?

    pip install -r requirements.txt
    pytest app/tests/test_deck.py
    
    pytest app/tests/test_game_state.py

 
I tested the state change and the deck instances with shuffling.