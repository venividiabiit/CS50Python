name = input("What is your name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# We are using the 'match' and 'case' keywords to make the code more succinctly
match name:
    case "Harry" | "Hermione" | "Ron": # The single bar '|' is used to combine here. This is more concise than 'if' statements
        print("Gryffindor")
    # case "Hermione":
    #     print("Gryffindor")
    # case "Ron":
    #     print("Gryffindor")
    case "Draco":
        print("Slytherin")
        print("Slytherin")
    case _: # the underscore character is used in other contexts, but here it's for whatever 'case' is not been handled.
        print("Who?")