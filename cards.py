# Author: Thomas Lane
# Date: 2021/10/13
"""A module that implements basic playing card functionality
"""

import pprint
import random
from typing import List, NamedTuple
from collections import namedtuple

# Tuple containing of suits from deck of cards
SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")

# Dictionary housing card numeric value / score indexed by face value
CARD_SCORES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}

# Allow card information to be access by name by using namedtuple.
# With a standard tuple the each piece of data could only be accessed by position.
Card = namedtuple("Card", "value suit")


def make_suit(suit: str) -> List[Card]:
    """
    Generates a list containing all of the cards in a single suit

    Args:
        suit (str): the suit for which to generate the cards

    Returns:
        List[Card]: a list containing all the cards in the suit.
                   each card is a Card tuple with the card value
                   followed by the suit in the format:

                   $Value, $Suit

                   Examples:

                        ('4', 'Hears')
                        ('8', 'Diamonds')
                        ('10', 'Clubs')
    """
    suit_cards: List[Card] = []

    for name in CARD_SCORES:
        card = Card(name, suit)
        suit_cards.append(card)

    return suit_cards


def make_deck() -> List[Card]:
    """
    Generates a list containing a card for each of the cards in a standard
    playing deck

    A "standard" deck of playing cards consists of 52 Cards in each of the 4
    suits of Spades, Hearts, Diamonds, and Clubs. Each suit contains 13 cards:
    Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King

    Returns:
        List[Card]: List containing card for each of the cards in a standard
                   deck.
    """
    deck: List[Card] = []

    for suit in SUITS:
        deck += make_suit(suit)

    return deck


def shuffle_deck(deck: List[Card]):
    """
    Shuffles deck of cards in place, i.e. modifies the passed deck parameter
    but doesn't return a new value

    Args:
        deck (List[Card]): List containing cards, with a card for all the cards
                            in a standard deck
    """
    random.shuffle(deck)


def deal_card(deck: List[Card]) -> Card:
    """Deal card (returning) from the start of the list of cards
    After dealing the card, the deck will no longer include the card

    Args:
        deck (List[Card]): the deck of cards from which to deal out cards

    Returns:
        Card: the card from the top (front) of the deck
    """
    card = deck.pop(0)

    return card


def main():
    # Create Deck of cards
    deck = make_deck()

    # Print Deck
    print("\nDeck:")
    pprint.pprint(deck)

    # Randomize the order of the cards in the deck
    shuffle_deck(deck)

    print("\nShuffled Deck:")
    pprint.pprint(deck)

    card1 = deal_card(deck)
    card2 = deal_card(deck)

    print("\nCards:")
    pprint.pprint(card1)
    print(f"Value of card1: {CARD_SCORES[card1.value]}")
    print(f"Value of card1: {CARD_SCORES[card1[0]]}\n")

    pprint.pprint(card2)
    print(f"Value of card2: {CARD_SCORES[card2.value]}")
    print(f"Value of card2: {CARD_SCORES[card2[0]]}\n")

    # Print the remaining cards in the deck
    print("\nDeck after Dealing Cards:")
    pprint.pprint(deck)


if __name__ == "__main__":
    main()
