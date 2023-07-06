enemies = 1


#this will return enemies = 2, because enemies is within the local scope. enemies 2 can only be accessed within the funciton, so you can't use the variable outside 
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()

print(f"enemies outside function: {enemies}")

#local scope - exists within a function.
#global scope - exists outside the function, available anywhere.