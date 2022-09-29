x = input("What's x? ")
y = input("What's y? ")

z = x + y # obviously, strings will be concatenated, therefore the result will be 1 + 2 = 12
z = int(x) + int(y) # add int and put (x) to convert to integer
# ^ this 'older' method, may be easier to debug.

print(z)

x = int(input("What's x? "))
y = int(input("What's y? "))
# ^ we are nesting the functions here, so that the return value of the inner function becomes the argument,
# to the input to the outer function. We don't need to create another variable now. Code lines
# are more succinct like this.

print(x + y)

print(int(input("What's x? ")) + int(input("What's y? ")))
# ^ maybe this is more concise. It's not very simple or clear, though.
# Nesting too many things together can be messy and a waste of time,
# not too mention complicating your code and increasing the chance it will get buggy.

x = float(input("What's x? "))
y = float(input("What's y? "))
# ^ and here we're using float() to set the number to a decimal point.

print(x + y)

#x = round(input("What's x? "))
#y = round(input("What's y? "))
x = float(input("What's x? "))
y = float(input("What's x? "))
# we can't use round() before float()

z = round(x + y)
# ^ we can round the number, a float will be rounded up to the nearest integer.

print(z)

print(f"{z:,}")
# ^ the :, will automatically format the number (for example 999 + 1) to 1,000.
# I believe this is slicing.
x = float(input("What's x? "))
y = float(input("What's x? "))

z = x / y

print(z)
# ^ Some final examples of float.

# Sidenote: int()'s, in Python nowadays can be as big as possible, but there's a ceiling how precise
# a float() can be.

x = float(input("What's x? "))
y = float(input("What's x? "))

z = round(x / y, 2)

print(f"{z:.2f}")
# ^ now it gets formatted with the format string. the .2f could be applied if variable z does not x / y, 2
# for instance.