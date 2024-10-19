# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order or arguments doesn't matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", first="Spongebob", last="Squarepants", title="Mr.")
# positional arguments must come before any keyword arguments
# here "Hello" is a positional argument and the rest are keyword arguments
