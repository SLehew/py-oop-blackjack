# classes - Deck, Card, Dealer, Player, Game
# create deck
# shuffle
# add player and dealer
# deal cards
# play hand
import random


SUITS = ['♥︎', '♦︎', '♣︎', '♠︎']
RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        deck_string = ''
        for card in self.cards:
            deck_string += str(card)
        return deck_string

    def shuffle(self):
        random.shuffle(self.cards)


class Dealer:
    def __init__(self):
        self.hand = []

    def __str__(self):
        return 'Dealer'

    def hit(self, card):
        self.hand.append(card)


class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name

    def hit(self, card):
        self.hand.append(card)


class Game:
    def __init__(self, suits, ranks):
        self.player = Player(self.get_player_name())
        self.dealer = Dealer()
        self.deck = Deck(suits, ranks)
        self.deck.shuffle()

    def get_player_name(self):
        name = input('What is your name?')
        return name


new_game = Game(SUITS, RANKS)
print(new_game.__dict__)


deck_of_cards = Deck(SUITS, RANKS)
deck_of_cards.shuffle()
print(deck_of_cards)
