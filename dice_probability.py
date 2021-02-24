from random import randint

class Dice:
    def __init__(self, sides = 6):
        self.sides = sides
        self.value = 1


    def roll(self):
        self.value = randint(1, 6)


dice = [Dice(), Dice()]

while True:
    try:
        rolls = int(input(f"How many rolls would you like to simulate?\n"))
        break
    except:
        print("Invalid entry.")

options = []
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for x in range(rolls):
    for die in dice:
        die.roll()
    options.append(dice[0].value)
    options.append(dice[1].value)
    options.append(dice[0].value + dice[1].value)

print(f"Results for {rolls:,} rolls of the dice")
print("number --> times activated every 100 rolls")
for p in possibilities:
    probability = round(options.count(p) / rolls * 100, 0)
    print(f"{p} --> {probability:.0f}")
