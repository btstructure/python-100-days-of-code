fruits = ["Strawberries", "Apples", "Peaches"]
vegetables = ["Tomato", "Carrot", "Cucumber"]

dirtydozen = [fruits, vegetables]

print(dirtydozen)
#dirty dozen has 2 lists inside it, there is an index for a list and within that list, is items which also have an index
#[['Strawberries', 'Apples', 'Peaches'], ['Tomato', 'Carrot', 'Cucumber']]

#will return strawberries because the first index points to fruits, and the second points to the first item in fruits
print(dirtydozen[0][0])