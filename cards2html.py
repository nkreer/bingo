import json, time

printstr = ""

with open("cards.json") as file:
    cards = json.load(file)

# Page layout
printstr += '''<html><head>
<style>
    body {
        font-family: sans-serif;
    }
    td {
        margin: 10px;
        padding: 15px;
        order-style: solid;
        border-radius: 10px;
        background-color: #e2e2e2;
    }
    @media print {
        footer {page-break-after: always;}
    }
</style>
</head><body>'''

cardNumber = 1
for index, card in enumerate(cards):
    printstr += "<h3>Bingo #" + str(index) + " - " + str(int(time.time())) + "</h3>"
    printstr += "<table>"

    # Populate the card with its pre-generated numbers
    c_i = 0
    for x in range(0, 4):
        printstr += "<tr>"
        for y in range(0, 4):
            printstr += "<td>" + str(card[c_i]) + "</td>"
            c_i += 1
        printstr += "</tr>"

    printstr += "</table><br><br><br>"

    # Make sure 3 cards are printed on the same A4 page
    if cardNumber == 3:
        printstr += "<footer></footer>"
        cardNumber = 0

    cardNumber += 1

# Save the generated HTML
printfile = open("cards.html", "w+")
printfile.write(printstr)
printfile.close()
