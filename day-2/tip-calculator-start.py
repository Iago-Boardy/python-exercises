print("Welcome to the tip calculator.")
total = input("How much was the total bill? $")
people = input("How many people to split the bill? ")
tip = input("What percentage tip would you like to give? 10, 12 or 15... ")

if tip == "10":
  tip = 1.10 
elif tip == "12":
  tip = 1.12
elif tip == "15":
  tip = 1.15

perPersonTotal = float(total) / int(people)
perPersonTotal = "{:.2f}".format(perPersonTotal * tip) 
#Here you could also format with the round(number, 2) method, but it was a little buggy

print(f"Each person shold pay: ${perPersonTotal}")


