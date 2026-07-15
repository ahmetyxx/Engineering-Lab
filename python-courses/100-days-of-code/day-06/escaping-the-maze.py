def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_back():
    turn_left()
    turn_left()
def walk_through_right():
    while front_is_clear() and wall_on_right():
                    move()
            
            
while not at_goal():
    if wall_on_right() and front_is_clear():
        walk_through_right()
        
    elif not wall_on_right() and wall_in_front():
        turn_right()
        move()
    
    elif not wall_on_right() and not wall_in_front():
        turn_right()
        while  not wall_in_front():
            move()

    
    elif wall_on_right() and wall_in_front():
        while wall_on_right() and wall_in_front():
            turn_left()