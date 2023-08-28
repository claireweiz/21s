* Source: [guardian coding exercises](https://github.com/guardian/coding-exercises).
* In README first section, it lists out the instructions of the exercises. In second section, it lists the structure of my codes.

## Can you beat the dealer at 21


#### Model the game
* create a single deck of playing cards
* two players (called Sam and the Dealer) who will play against each other
* each player is given two cards from the top of a shuffled deck of cards

#### Rules to implement
* determine score of a hand[^1]
* check if either player has blackjack (21) with their initial hand and wins the game
* if neither player has blackjack then Sam can start drawing cards from the top of the deck
* Sam should stop drawing cards from the deck if their total reaches 17 or higher
* Sam has lost the game if their total is higher than 21 
* when Sam has stopped drawing cards the Dealer can start drawing cards from the top of the deck
* the Dealer should stop drawing cards when their total is higher than Sam.
* the Dealer has lost the game if their total is higher than 21 
* determine which player wins the game

[^1]: Numbered cards are their point value. Jack, Queen and King count as 10 and Ace counts as 11.


## My solutions

* Updated Aug 28, 2023
* Using Object Oriented Programming concepts to create the program.
* Import the random module
* Create Class Card, Deck, Hand, Game
* Class Deck: shuffle the cards and get deck ready
* Class Hand: caculate value (card score)
* Class Card: present both card and value
* Class Game: run the game in command line