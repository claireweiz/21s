import random

# Card class represents a playing card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Deck class represents a deck of cards
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


# Hand class represents a player's or dealer's hand
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.rank in ["Jack", "Queen", "King"]:
                value += 10
            elif card.rank == "Ace":
                value += 11
                num_aces += 1
            else:
                value += int(card.rank)
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value


# Game class represents the blackjack game
class Game:
    def __init__(self):
        self.deck = Deck()
        self.sam = Hand()
        self.dealer = Hand()

    def deal_initial_cards(self):
        for _ in range(2):
            self.sam.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())

    def play(self):
        self.deal_initial_cards()

        print("Sam's cards:", *[str(card) for card in self.sam.cards])
        print("Sam's total:", self.sam.get_value())

        if self.sam.get_value() == 21:
            print("Sam has Blackjack! Sam wins.")
        else:
            self.play_sam()
            self.play_dealer()
            self.determine_winner()

    def play_sam(self):
        while self.sam.get_value() < 17:
            self.sam.add_card(self.deck.draw_card())
        print("Sam's final cards:", *[str(card) for card in self.sam.cards])
        print("Sam's final total:", self.sam.get_value())

    def play_dealer(self):
        while self.dealer.get_value() < self.sam.get_value() <= 21:
            self.dealer.add_card(self.deck.draw_card())
        print("Dealer's final cards:", *[str(card) for card in self.dealer.cards])
        print("Dealer's final total:", self.dealer.get_value())

    def determine_winner(self):
        sam_score = self.sam.get_value()
        dealer_score = self.dealer.get_value()

        if sam_score > 21:
            print("Sam busts. Dealer wins.")
        elif dealer_score > 21:
            print("Dealer busts. Sam wins.")
        elif sam_score > dealer_score:
            print("Sam wins!")
        elif sam_score < dealer_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")


# Main game loop
def main():
    print('❤️♥️♣️♦️ 21s')
    game = Game()
    game.play()


if __name__ == "__main__":
    main()