
enemies = 1


# #will return an error
# def increase_enemies():
#     enemies += 1
#     print(f"enemies  inside function, {enemies}")

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies  inside function, {enemies}")

increase_enemies()

#avoid modifying global scopes
#usually have a global scope for something you don't want to look over. Uppercase it is best practice.
#PI 3.14159