#dictionary - a table with a key and value.

#to create a dictionary {Key: Value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

#in a dictionary you add square brackets with the key instead of the index

print(programming_dictionary["Bug"])

#Adding new items to dictionary, but if the key already exists it'll replace the value by what you set to equal too
# programming_dictionary["Loop"] =  "The action of doing something over and over again."
#print(programming_dictionary)

# #creating an empty dictionary
# empty_dictionary = {}
# #or you can do it to wipe an existing dictionary
# programming_dictionary = {}

for key in programming_dictionary:
    print(key) #will print the key and not the value
    print(programming_dictionary[key]) #will print the value based on the key