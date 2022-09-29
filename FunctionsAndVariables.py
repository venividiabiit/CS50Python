# input inbuilt function.  "" string is an argument.
name = input("What is your name?") # assigning input to x
# will make the input print out below.
# ^ input will expect a string, that is text (so no int/float/complex
print("Hello, " + name.title() + ".")
# ^ I already know most of this.
# pseudocode is for outlining the program you're coding.
""""
Many many many lines
of comments.
"""
print("hello, " + name)
# we know of concatenation already.
print("hello,", end="")
# this will add name, with the , outside the string, also adds space.
print("hello", name, sep=",")
# ^ using a sep
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# ^ here we have the crazy cryptic thing with lots of parameters.
#print("Hello, ""name"")
# ^ wont run, use '' single quotes instead.
print('Hello, "name"')
# ^ like this
print("Hello, \"name\"")
# ^ literal quotes.

name = name.strip()
# ^ this will remove whitespace from str
name = name.capitalize()
# ^ this will capitalize, but only the first letter in the string.
name = name.title()
# ^ titles is the better options

name = name.strip().title()
# but let's chain the functions(Methods) together,
# didn't know this could be done ^_^. Technically,
# combinations can be infinite, but should not be done for grammatical
# purposes.
print(f"hello, {name}.")
# ^ format string (put f before quotations), i remember
# this from Mr. Buchalka,
name = input("What is your name? ").strip().title()
print(f"Hello {name}")

print('   spacious   '.strip().upper()).split()
# ^ space in the middle is difficult to remove.
# we already know of lstrip() and rstrip()
# reading the documentation on docs.python.org is
# recommendable.
#first, last = name.split(" ")