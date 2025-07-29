
hand_1 = ["A","5","9"]
hand_2 = ["3","4"]
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    pass
    
    total_hand1 = 0
    cuenta_as = 0
    for card in hand_1:
        if card.lower() == "j":
            total_hand1 = total_hand1 + 10
        elif card.lower() == "q":
            total_hand1 = total_hand1 + 10
        elif card.lower() == "k":
            total_hand1 = total_hand1 + 10
        elif card.lower() == "a":
            cuenta_as = cuenta_as + 1
        else:
            total_hand1 = total_hand1 + int(card)
    
    if total_hand1 <= 20:
        if cuenta_as == 1 and total_hand1 + 11 > 21:
            total_hand1 = total_hand1 + 1
        elif cuenta_as == 1 and total_hand1 + 11 <= 21:
            total_hand1 = total_hand1 + 11
        elif cuenta_as == 2 and total_hand1 + 12 > 21: 
            total_hand1 = total_hand1 + 2
        elif cuenta_as == 2 and total_hand1 + 12 <= 21:
            total_hand1 = total_hand1 + 12
        elif cuenta_as == 3 and total_hand1 + 13 > 21:
            total_hand1 = total_hand1 + 3
        elif cuenta_as == 3 and total_hand1 + 13 <= 21:
            total_hand1 = total_hand1 + 13
        elif cuenta_as == 4 and total_hand1 + 14 > 21:
            total_hand1 = total_hand1 + 4
        elif cuenta_as == 4 and total_hand1 + 14 <= 21:
            total_hand1 = total_hand1 + 14 
    else:
        return False

    total_hand1 = 0
    cuenta_as = 0
    for card in hand_1:
        if card.lower() == "j":
            total_hand1 = total_hand1 + 10
        elif card.lower() == "q":
            total_hand1 = total_hand1 + 10
        elif card.lower() == "k":
            total_hand1 = total_hand1 + 10
        elif card.lower() == "a":
            cuenta_as = cuenta_as + 1
        else:
            total_hand1 = total_hand1 + int(card)
    
    if total_hand1 <= 20:
        if cuenta_as == 1 and total_hand1 + 11 > 21:
            total_hand1 = total_hand1 + 1
        elif cuenta_as == 1 and total_hand1 + 11 <= 21:
            total_hand1 = total_hand1 + 11
        elif cuenta_as == 2 and total_hand1 + 12 > 21: 
            total_hand1 = total_hand1 + 2
        elif cuenta_as == 2 and total_hand1 + 12 <= 21:
            total_hand1 = total_hand1 + 12
        elif cuenta_as == 3 and total_hand1 + 13 > 21:
            total_hand1 = total_hand1 + 3
        elif cuenta_as == 3 and total_hand1 + 13 <= 21:
            total_hand1 = total_hand1 + 13
        elif cuenta_as == 4 and total_hand1 + 14 > 21:
            total_hand1 = total_hand1 + 4
        elif cuenta_as == 4 and total_hand1 + 14 <= 21:
            total_hand1 = total_hand1 + 14 
    else:
        return False    
    print(cuenta_as)
    print(total_hand1)  
    
    
    

blackjack_hand_greater_than(hand_1, hand_2)
