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


def generate_actions(state):
    raise NotImplementedError("This function is not implemented yet.")


def apply_action(state, action, next_card=None):
    raise NotImplementedError("This function is not implemented yet.")def parse_state(text):
    hand_str, dealer_str, turn_str = [x.strip() for x in text.split("|")]

    hand = [card.strip() for card in hand_str.split(",")]

    return {
        "hand": hand,
        "dealer": dealer_str,
        "first": turn_str == "first"
    }


def generate_actions(state):
    actions = ["Hit", "Stand"]

    if state["first"]:
        actions.append("Double Down")
        actions.append("Surrender")

        if state["dealer"] == "A":
            actions.append("Insurance")

        if (
            len(state["hand"]) == 2
            and state["hand"][0] == state["hand"][1]
        ):
            actions.append("Split")

    return actions


def apply_action(state, action, next_card=None):
    hand = state["hand"][:]

    if action not in generate_actions(state):
        raise ValueError("Illegal action.")

    if action == "Hit":
        if next_card is None:
            raise ValueError("Hit requires next_card.")
        hand.append(next_card)
        return hand

    if action == "Stand":
        return hand

    if action == "Double Down":
        if next_card is None:
            raise ValueError("Double Down requires next_card.")
        hand.append(next_card)
        return hand

    if action == "Insurance":
        return hand

    if action == "Surrender":
        return "Surrender"

    if action == "Split":
        return [
            [hand[0]],
            [hand[1]]
        ]

    raise ValueError("Unknown action.")

    
