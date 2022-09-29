x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")
# if x >= y:
#     print("x is greater than or equal to y")
# if x <= y:
#     print("x is lesser or equal to y")
elif x > y:
    print("x is greater than y")
# elif x == y:
#     print("x is equal to y")
# elif x != y:
#     print("x is not equal to y") # this is unneeded, the control flow will only assume > => < <= ==
else:
    # print("You need to learn how to code, idiot")
    print("x is equal to y")