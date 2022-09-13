# Authors
# Ryan Chan: A01031389
# Set A

"""
    This program simulates a game of blackjack.
    Multiple games can be played in a row, and total wins/losses will be shown at the end
    An option is given to play the game with no limit to how many cards can be drawn
"""

from typing import List
import cards


def player_draw_another(hand: list, deck: list) -> bool:
    """Draws another cards if the player selects Y

    Args: hand, deck
    """
    user_input = input('Would you like another card (Y/N) ')
    if (user_input[0].upper() == "Y"):
        hand.append(cards.deal_card(deck))
        return True
    else:
        return False

def display_card_string(hand: list, position: int) -> str:
    """Displays the card's position hand, value, and suit

    Args: hand, position
    """
    return "Card(value='" + hand[position][0] + "', suit='" + hand[position][1] + "')"


def print_final_scores(playerHand: list, compHand: list, playerScore: int, compScore: int):
    """Prints both player and computer hands and displays each hand's total

    Args: playerHand, compHand, playerScore, compScore
    """
    player_final_hand = []
    comp_final_hand = []

    i = 0
    while i < len(playerHand):
        player_final_hand.append(display_card_string(playerHand, i))
        i += 1

    i = 0
    while i < len(compHand):
        comp_final_hand.append(display_card_string(compHand, i))
        i += 1

    print('Player 1 Score:', playerScore)
    print('Player 1 Hand [' + ', '.join(player_final_hand) + ']\n')
    print('Computer Score:', compScore)
    print('Computer Hand [' + ', '.join(comp_final_hand) + ']\n')

def calculateTotal(hand: list) -> int:
    """
    Calculates the total for a given hand

    Args: hand

    Returns: total (int)
    """
    aceInHand = 0
    total = 0

    i = 0
    while i < len(hand):
        if hand[i][0] != "Ace":
            total += cards.CARD_SCORES[hand[i][0]]
        else:
            aceInHand += 1
        i += 1
    
    j = 0
    while j < aceInHand:
        if total <= 10:
            total += 11
        else:
            total += 1
        j += 1

    return total



def determineWinner(playerHand: list, compHand: list, deck: list) -> bool:
    """
    Declares if result is Bust, Win, Lose, or Standoff (Tie)

    Calls print_final_scores() function to display scores

    Args: playerHand, compHand, deck

    Returns: player_win Boolean
    """
    playerTotal = 0
    compTotal = 0
    player_win = False

    playerTotal = calculateTotal(playerHand)
    compTotal = calculateTotal(compHand)

    if playerTotal > 21:
        print("You Bust\n")
    elif ((playerTotal > compTotal) or (compTotal > 21)):
        print("You Win\n")
        player_win = True
    elif (playerTotal < compTotal):
        print("You Lose\n")
    elif (playerTotal == compTotal):
        print("Standoff: Dealer Wins\n")

    print_final_scores(playerHand, compHand, playerTotal, compTotal)

    return player_win




def play_game():
    """play one game of blackjack
    
    playerHand: list of cards in the player's hand
    compHand: list of cards in the computer's hand
    unlimitedMode: flag to set the game to unlimited draw mode

    Returns:
        bool: True if the player wins
    
    """
    deck = []
    playerHand = []
    compHand = []
    displayHand = []
    unlimitedMode = False

    while True:
        user_input = input('Would you like to play with unlimited cards? (Y/N) ')
        if (user_input[0].upper() == "Y"):
            unlimitedMode = True
        break

    deck = cards.make_deck()
    cards.shuffle_deck(deck)

    print('Dealing Cards\n')
    for i in range(0,2):
        playerHand.append(cards.deal_card(deck))
        compHand.append(cards.deal_card(deck))

    print('Computer card 1: hidden')
    print('Player Card 1: ' + display_card_string(playerHand, 0))
    print('Computer Card 2: ' + display_card_string(compHand, 1))
    print('Player Card 2: ' + display_card_string(playerHand, 1))


    print()
    
    if unlimitedMode:
        while unlimitedMode:
            unlimitedMode = player_draw_another(playerHand, deck)
            if (calculateTotal(compHand) < 21):
                compHand.append(cards.deal_card(deck))
            i = 0
            while i < len(playerHand):
                displayHand.append(display_card_string(playerHand,i))
                i += 1
            print('Player 1 Hand [' + ', '.join(displayHand) + ']\n')
            displayHand = []

    else:
        player_draw_another(playerHand, deck)
        if (calculateTotal(compHand) < 21):
            compHand.append(cards.deal_card(deck))
        i = 0
        while i < len(playerHand):
            displayHand.append(display_card_string(playerHand,i))
            i += 1
        print('Player 1 Hand [' + ', '.join(displayHand) + ']\n')

    print('Computer Card 1: ' + display_card_string(compHand, 0) + '\n')

    return determineWinner(playerHand, compHand, deck)



def main():
    """Increments wins and losses according to games
    
    runs functions as long as keep_playing Boolean is True, breaks if player no longer wants to play

    Result: Number of Wins and Losses the Player has
    """

    keep_playing = True
    wins = 0
    losses = 0
    while keep_playing:

        if (play_game()):
            wins += 1
        else:
            losses += 1

        user_continue = input('Would you like to play again? (Y/N) ')

        if user_continue[0].upper() != 'Y':
            keep_playing = False

    print(f'Wins {wins} Losses: {losses}\n')

    print('Exiting...')

if __name__ == '__main__':
    main()