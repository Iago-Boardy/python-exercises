line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

import re

separated = re.findall(r'\D|\d+', position)
horizontal = separated[0].upper()
vertical = int(separated[1]) -1

if horizontal == 'A':
  horizontal = 0
elif horizontal == 'B':
  horizontal = 1
elif horizontal == 'C':
  horizontal = 2

map[vertical][horizontal] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
