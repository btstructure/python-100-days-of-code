#while loop - will continue going through a loop until the condition is no longer true
#while key word

a = 0
while a < 5:
    a += 1
    print(a)

#hurdles using the while loop
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_down():
    turn_left()
    turn_left()

def robot_moves():
    while at_goal() != True:
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
robot_moves()