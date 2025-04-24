some_string = "my name is masha SSSSSS 4723875428572  namer"
upper = some_string.upper()
lower = some_string.lower()
title = some_string.title()
capitalize = some_string.capitalize()
chaain = some_string.lower().upper().capitalize()

clear_string_spaces = some_string.strip()
clear_string_symbols = some_string.strip(" name")

change_inner_text = (
    some_string.replace("name", "surname", 1)
    .replace("masha", "Masha")
    .replace("namer", "")
)
change_inner_text_symbols = some_string.replace("name", "surname", 1)
table = str.maketrans("42", "24", "my")
result_smart_change = some_string.translate(table)

# slices

slices1 = some_string[:]
slices2 = some_string[0:10]
slices3 = some_string[10:15]
slices4 = some_string[::2]
pass
