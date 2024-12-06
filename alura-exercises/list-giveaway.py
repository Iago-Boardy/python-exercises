import random


def main():
    p = int(input("Type the number of people that are participating: "))
    people = []

    for i in range(p):
        people.append(i + 1)


    lucky_one = random.choice(people)

    print(f"The lucky person today is the {lucky_one}° one!")


if __name__ == "__main__":
    main()