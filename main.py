# TODO welcome to MAU. The only rule you will be told is this one
# Press Q to learn the rest of the rules

# TODO help button for game rules that delivers a penalty


# Set up game
suites = ["ace", "club", "spade", "diamond"]
cards = ["one", "two", "three"]

def shuffle_deck():
    return 0

# set up players
def get_players():
    return 0
players = {"Player 1":"dylan", "Player 2":"Barbara"}


def hand_out_cards():
    return 0
hands_of_cards = {}

# begin game

def play_card():
    card_selection = input(print("What card do you want to play?"))
    return card_selection

card_selected = play_card()
used_up_cards = []

# rules

def check_if_same_suite(i):
    if i/2 == 2:
        print("is even")

def check_if_same_number(i):
    print(i)
    return 0

rules = [check_if_same_suite, check_if_same_number]

def check_rules(card_selection):
    for rule in rules:
        rule(card_selection, used_up_cards[-1])

# TODO a function to check if someone has said mau
