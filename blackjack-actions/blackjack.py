RANK_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11,
}


def hand_value(cards):
    total = sum(RANK_VALUES[card] for card in cards)
    aces = cards.count("A")
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


def parse_state(text):
    hand_str, dealer_upcard, flag = [part.strip() for part in text.split("|")]
    hand = [rank.strip() for rank in hand_str.split(",")]

    return ...


def generate_actions(state) :
    hand, dealer_card, flag=state
    value= hand_value (hand) 
    if value >= 21
    return ["stand"] 
    else
    return ["hit"] 

def apply_action(state, action, next_card= none):
    and, delear_card, flag=state
    f action= "hit" and next_card:
    hand. append(next_card)
    return (hand, delear_card, flag) 
elif action="stand"
return(hand,dealer_card,flag)
return state

    








    





                              





                              











                 






                 
    rais




