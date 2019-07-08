import random, curses, json, textwrap
from curseXcel import Table

with open("cards.json") as file:
    cards = json.load(file)

# Possible lines with corresponding line names
lines = {
    "H1": [0, 1, 2, 3],
    "H2": [4, 5, 6, 7],
    "H3": [8, 9, 10, 11],
    "H4": [12, 13, 14, 15],
    "V1": [0, 4, 8, 12],
    "V2": [1, 5, 9, 13],
    "V3": [2, 6, 10, 14],
    "V4": [3, 7, 11, 15],
    "B": list(range(0, 16))
}

stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

screen_height, screen_width = stdscr.getmaxyx()

# 1-99 and randomize them
numbers = list(range(1, 100))
random.shuffle(numbers)
called_out = []

# Call out the numbers
for number in numbers:
    # Draw out the player table along with their line information
    table = Table(stdscr, len(cards), len(lines) + 1, 4, screen_width, screen_height - 2, spacing=1, col_names=True)

    # Draw the col headers
    table.set_column_header("P", 0)
    count = 1
    for line, value in lines.items():
        table.set_column_header(line, count)
        count += 1

    # Populate the table
    for index, card in enumerate(cards):
        # Required for drawing in the correct place
        table.set_cell(index, 0, str(index))
        line_index = 1
        # Check for the completion of all lines
        for line_name, line in lines.items():
            everything = True
            # Scan each individual field of the line
            for field in line:
                if card[int(field)] not in called_out:
                    everything = False

            if everything:
                table.set_cell(index, line_index, "Yes")
            else:
                table.set_cell(index, line_index, " ")

            line_index += 1

    table.refresh()

    # Keep track of the numbers already called out
    called_out.append(number)

    # Save the already called out numbers to a file for reference
    called_out_file = open("called.txt", "w+")
    called_out_file.write(str(called_out))
    called_out_file.close()

    stdscr.addstr(screen_height - 1, 0, "Current number: " + str(number) + " || Remaining draws: " + str(len(numbers) - len(called_out)))

    stdscr.getch()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

print("The game has ended!")
