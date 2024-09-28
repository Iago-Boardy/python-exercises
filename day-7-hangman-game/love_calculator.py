def calculate_love_score(n1, n2):
    names = (n1.upper() + n2.upper()).replace(" ", "")
    value1 = 0
    value2 = 0
    for i in names:
        if i in "TRUE":
            value1 += 1
        if i in "LOVE":
            value2 += 1

    return str(value1) + str(value2)


print(calculate_love_score("Kanye West", "Kim Kardashian"))
