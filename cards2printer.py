import json, time
from escpos.printer import Usb

printer = Usb(0x0416, 0xaabb)

with open("cards.json") as file:
    cards = json.load(file)

for index, card in enumerate(cards):
    printer.text("Bingo #" + str(index) + "\n\n")

    # Populate the card with its pre-generated numbers
    for x in range(0, 16):
        printer.text(str(card[x]) + "   ")
        if (x + 1) % 4 == 0:
            printer.text("\n")

    printer.text("\n---\n\n\n")
