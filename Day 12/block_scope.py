#there is no block scope in python


enemies = ["Skeleton", "Zombie", "Alien"]

game_level = 3

if game_level < 5:
    new_enemy = enemies[0]

#will return skeleton despite being within the if statement
print(new_enemy)

#will return skeleton despite being within the if statement
print(new_enemy)

def create_enemy():
    if game_level < 5:
        new_enemy_2 = enemies[0]
        
        print(new_enemy_2)

#doesn't exist when it is within a function
# print(new_enemy_2)