import json
import random

card_amount = int(input("How many players will there be? "))
card_min = 1
card_max = 99

cards = []


# Generate a single card
def generateRandomCard(minimum, maximum):
    card = []

    # Fill the card with 16 different random numbers in the specified range
    while len(card) < 16:
        number = random.randint(minimum, maximum)
        if number not in card:
            card.append(number)

    card.sort()
    return card


# Generate the specified amount of cards and make sure no card is issued twice
while len(cards) < card_amount:
    card = generateRandomCard(1, 99)
    if card not in cards:
        cards.append(card)

with open("cards.json", "w+") as file:
    json.dump(cards, file, indent=2)
