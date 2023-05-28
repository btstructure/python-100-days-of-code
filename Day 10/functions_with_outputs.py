def format_name(f_name,l_name):
    print(f_name.title())
    print(l_name.title())


format_name("bilbo", "BAGGINS")

# def formated_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     #the return keyword means it is the end of the function
#     return f"{formated_f_name} {formated_l_name}"

# formated_string = formated_name("bILbo", "BAggins")
# print(formated_string)

def formated_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return 
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    #the return keyword means it is the end of the function
    return f"{formated_f_name} {formated_l_name}"
#will return none 
formated_string = formated_name("", "BAggins")
print(formated_string)