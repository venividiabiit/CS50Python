def main():
    x = int(input("What is x? "))
    if is_even(x): # this Function is called now, even thought it's down the line.
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
# When creating our own functions, we can use Python's inbuilt functions (example: strip, upper, lower, etc). But only
# on things that the function is used for (for example strings or booleans)


main()

# def is_even(n):
#     return True if n % 2 == 0 else False

# ^ We can also make the function more "Pythonic", more elegantly formulated. I agree with Mr. Malan, this looks
# more efficient.

# is_even()

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# def isEven():
#     if x % 2 == 0:
#         print("Even")
#
# def isOdd():
#     if x % 2 != 0:
#         print("Odd")
# The standard is to call the first created function main(). We have refrained from doing so here.

# isEven() # we are calling the Functions isEven() and isOdd() here.
# isOdd()