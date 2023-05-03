#strings - a string of characters

a = "george"
print(type(a))

#integers

b = 5
print(type(b))

#floats 

c = 120.56

print(type(c))

#booleans

print(type(1==1))


#type errors

#the error below is a type error, 
# num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")

num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")