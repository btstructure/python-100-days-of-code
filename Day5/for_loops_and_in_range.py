#range function - generates a range of number to loop through

#will print all the numbers in the range except 100, because the 100 is exclusive
# for number in range(0, 100):
#     print(number)

#the 3 is steps, so the loop will return the values by 3
# for number in range(0, 100, 3):
#     print(number)


total = 0

for number in range(0,101):
    total += number
print(total)