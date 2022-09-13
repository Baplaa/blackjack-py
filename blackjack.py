# Author
# Tristan Lingat: 01270360
# Set A

"""
    This program is a game of blackjack against the player and computer.

    An unlimited mode is supported:
        no limits to draw cards

    If the player chooses, they can run through multiple games

    A total of player wins and losses is counted and shown when they decide to end the game(s)
"""

from typing import List
import cards

def p_draw(hand, deck):
    """Should the player chooses to draw another card, draw another card!

    Args: hand, deck

    Return: boolean
    """
    p_input = input('Would you like another card? (Y/N) ')
    if p_input[0].upper() == 'Y':
        hand.append(cards.deal_card(deck))
        return True
    else:
        return False

def card_info(hand, position):
    """Shows the value of the card alongisde its suit and hand position

    Args: hand, position

    Returns: card_details
    """
    card_details = "the " + hand[position][0] + " of " + hand[position][1]
    return card_details

def card_counter(p_hand, pc_hand, p_score, pc_score):
    """Both the player and computer's hands and total card count are printed

    Args: p_hand, pc_hand, p_score, pc_score
    """
    finalp_hand = []
    finalpc_hand = []

    i = 0
    while i < len(p_hand):
        p_call = card_info(p_hand, i)
        finalp_hand.append(p_call)
        i += 1

    i = 0
    while i < len(pc_hand):
        pc_call = card_info(pc_hand, i)
        finalpc_hand.append(pc_call)
        i += 1 
    
    print("Player 1's Score is ", p_score)
    print('Their Hand is [' + ', '.join(finalp_hand) + ']\n')
    print("Computer's Score is ", pc_score)
    print('Their Hand is [' + ', '.join(finalpc_hand) + ']\n')

def total(hand):
    """Calculates the total sum of a hand

    Args: hand

    Returns: total
    """
    ace_count = 0
    total = 0

    i = 0
    while i < len(hand):
        if hand[i][0] != "Ace":
            total += cards.CARD_SCORES[hand[i][0]]
        else:
            ace_count += 1
        i += 1

    i1 = 0
    while i1 < ace_count:
        if total <= 10:
            total += 11
        else:
            total += 1
        i1 = 1
    
    return total

def match_result(p_hand, pc_hand):
    """Prints the match results then calls card_counter

    Args: p_hand, pc_hand

    Returns: p_win
    """
    p_total = 0
    pc_total = 0
    p_win = False

    p_total = total(p_hand)
    pc_total = total(pc_hand)

    if pc_total == p_total:
        print("Match Tie...Dealer Wins!\n")
    elif p_total < pc_total:
        print("Player 1 Loses!\n")
    elif (p_total > pc_total) or (pc_total > 21):
        print("Player 1 Wins!\n")
        p_win = True
    elif p_total > 21:
        print("Player 1 Busts!\n")

    card_counter(p_hand, pc_hand, p_total, pc_total)

    return p_win
    
    
def play_game():
    """play one game of blackjack or unlimited mode

    Returns: 
        bool: True if the player wins
    """
    deck = []
    p_hand = []
    pc_hand = []
    hand_info = []
    unlimited = False
    
    while True:
        ask_unlimited = input("Would you like to play 'Unlimited Mode'? (Y/N) ")
        if ask_unlimited[0].upper() == "Y":
            unlimited = True
        break

    deck = cards.make_deck()
    cards.shuffle_deck(deck)

    print('Dealing Cards...')
    
    for i in range(0,2):
        p_hand.append(cards.deal_card(deck))
        pc_hand.append(cards.deal_card(deck))

    print("Computer's Card 1 is HIDDEN!")
    print("Player 1's 1st Card is " + card_info(p_hand, 0))
    print("Computer's 2nd Card is " + card_info(pc_hand, 1))
    print("Player 1's 2nd Card is " + card_info(p_hand, 1))

    print()

    if unlimited:
        while unlimited:
            unlimited = p_draw(p_hand, deck)
            if total(pc_hand) < 21:
                pc_hand.append(cards.deal_card(deck))
            i = 0
            while i < len(p_hand):
                hand_info.append(card_info(p_hand, i))
                i += 1
            print('Player 1 Hand is [' + ', '.join(hand_info) + ']\n')
            hand_info = []

    else:
        p_draw(p_hand, deck)
        if total(pc_hand) < 21:
            pc_hand.append(cards.deal_card(deck))
        i = 0
        while i < len(p_hand):
            hand_info.append(card_info(p_hand, i))
            i += 1
        print('Player 1 Hand is [' + ', '.join(hand_info) + ']\n')

    
    print("Computer's 1st Card is " + card_info(pc_hand, 0))

    return match_result(p_hand, pc_hand)
    

def main ():
    """Keeps track of player's wins and losses and prints them once the player wants to stop playing blackjack
    """
    keep_playing = True
    wins = 0
    losses = 0
    while keep_playing:
        if play_game():
            wins += 1
        else:
            losses += 1

        user_continue = input('Would you like to play again? (Y/N) ')
        if user_continue[0].upper() != 'Y':
            keep_playing = False

    print(f'Win: {wins} Losses: {losses}\n')
    print('GG!')

if __name__ == '__main__':
    main()