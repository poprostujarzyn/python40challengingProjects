
print("Welcome to the Multiplication/Exponent Table App")

name = input("\nHello, what is your name: ").strip().capitalize()
number = float(input("What number would you like to work with: "))

print("\nMultiplication table for", number, "\n")
for i in range(1,10):
    print("\t", i, "*", number, "=", round(i*number, 4))


print("\nExponent table for", number, "\n")
for i in range(1,10):
    print("\t", number, "**", i, "=", round(number**i, 4))


message = name + " math is cool!"
print("\n")
print(message)
print("\t", message.lower())
print("\t\t", message.title())
print("\t\t\t", message.upper())





