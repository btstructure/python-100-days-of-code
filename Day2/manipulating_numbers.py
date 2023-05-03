#when using int, the numbers after the decimal places get removed. The type is a float

print(int(8/3))
print(type(8/3))

#you can also use round, which roounds to the decimal place you wish

print(round(8/3))

#you can put a number depending on how many places you wish to round it

print(round(8/3, 2))


#you can also do floor division
#unlike normal

print(8 // 3)
print(type(8 // 3_))