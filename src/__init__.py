# ask the user for their name
name = input("What's your name?")
name = name.strip().title()
print(f"hello,{name}")
# code calculate function
x = float(input("What's x?"))
y = float(input("What's y?"))
z = round(x + y)
print(x + y)
print(z)
a = x / y
print(a)
b = round(x / y, 2)
print(b)
print(f"{z:.2f}")


def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)


main()
