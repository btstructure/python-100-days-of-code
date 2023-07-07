# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
#   print("You can drive at age {age}.")



#   File "/root/python-udemy-course/Day 13/debugging_4.py", line 8, in <module>
#     if age > 18:
# TypeError: '>' not supported between instances of 'str' and 'int'
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

