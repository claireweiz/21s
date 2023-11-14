* There are two sections in README. 
* In the [first section](https://github.com/claireweiz/21s#can-you-beat-the-dealer-at-21), it's the coding instruction from the [Guardian coding exercises](https://github.com/guardian/coding-exercises) repo. 
* In the [second section](https://github.com/claireweiz/21s#my-solutions), it's my thought process and code structure.

## Can you beat the dealer at 21?


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
* I used an object-oriented programming structure to create the program

How I did this task:
* Import the random module
* Create the following classes: Deck, Hand, Card, and Game
* class Deck: shuffle the cards and get deck ready
* class Hand: calculate value (card score)
* class Card: present both card and value
* class Game: run the game in command line