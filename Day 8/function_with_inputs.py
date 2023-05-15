#practicing with functions again

# def greetings():
#     print("Hello!")
#     print("Hi!")
#     print("Goodmorning.")

# greetings()

#using parameters, greet is the parameter, when calling the function, pass the value you wish to pass 

def greeting(greet):
    print(greet)

greeting("hello")

def greeting_with_name(greet, name):
    print(f"{greet} my name is {name}")

#the values in the parentheses is the argument we are passing
greeting_with_name("hello","george")