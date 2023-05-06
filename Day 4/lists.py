#list - a data structure, organizing and storing data in python, a set of square brackets with items stored inside

#the values in the list have an index that starts with a 0
state_of_americas = ["Delaware", "New Jersey", "Georgia"]

print(state_of_americas)

print(state_of_americas[1])



#to manipulate the list you can use the index and then change the item

state_of_americas[1] = "New York"

print(state_of_americas)
# ['Delaware', 'New York', 'Georgia']

#adds a item into the end of the list
state_of_americas.append("Texas")
print(state_of_americas)

