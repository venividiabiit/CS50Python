score = int(input("Score: "))

# if score >= 90 and score <= 100:
#     print("Grade A: ")
# elif score >= 80 and score <= 90:
#     print("Grade B: ")
# elif score >= 70 and score <= 80:
#     print("Grade C: ")
# elif score >= 60 and score <= 70:
#     print("Grade D: ")
# else:
#     print("Grade F:")

# We are switching things around now.

# if 90 <= score and score <= 100:
#     print("Grade A: ")
# elif 80 <= score and score <= 90:
#     print("Grade B: ")
# elif 70 <= score and score <= 80:
#     print("Grade C: ")
# elif 60 <= score  and score <= 70:
#     print("Grade D: ")
# else:
#     print("Grade F:")
#
# # The below case is just like in paper-and-pencil example of equations
# if 90 <= score <= 100:
#     print("Grade A: ")
# elif 80 <= score <= 90:
#     print("Grade B: ")
# elif 70 <= score <= 80:
#     print("Grade C: ")
# elif 60 <= score <= 70:
#     print("Grade D: ")
# else:
#     print("Grade F:")

# or like this. Code that's succinct is arguably more maintanable long term.

if score >= 90:
    print("Grade A: ")
elif score >= 80:
    print("Grade B: ")
elif score >= 70:
    print("Grade C: ")
elif score >= 60:
    print("Grade D: ")
else:
    print("Grade F:")

# using only 'if' statements will print all Grade, will not make them mutually exclusive.
# if score >= 90:
#     print("Grade A: ")
# if score >= 80:
#     print("Grade B: ")
# if score >= 70:
#     print("Grade C: ")
# if score >= 60:
#     print("Grade D: ")
# else:
#     print("Grade F:")

# Things can also be constructed into Loops, but these are not in our vocabulary for now.