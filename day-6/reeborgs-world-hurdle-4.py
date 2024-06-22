def turn_right():
    for _ in range(3):
        turn_left()

while not at_goal():
    if wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move()
    else:
        turn_right()
        move()
