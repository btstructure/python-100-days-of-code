#fucntions with more than 1 input

def greet_with(name, location):
    print(f"Hello, my name is {name} and I live in {location}")

#positional argument, the order of the arguments go by the order of the parameters
greet_with("Alex", "NYC")

#keyword arguments

def greet_with(name = "Alex", location="NYC"):
    print(f"Hello, my name is {name} and I live in {location}")