def formated_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return 
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    #the return keyword means it is the end of the function
    return f"{formated_f_name} {formated_l_name}"
#will return none 
#if you hover over formated_name, the doc string that was put into the function will display. A good way to document what your function is doing
formated_string = formated_name("", "BAggins")
print(formated_string)