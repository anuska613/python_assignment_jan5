def div(x,y):
    print("{} / {} = {}".format(x,y,x/y))

def mul(x,y):
    print("{} / {} = {}".format(x,y,x*y))

math = {
    "1": div,
    "2": mul
}

x=int(input('Enter first number:'))
y=int(input('Enter second number:'))

print('1. Division.\n2. Multiply')
choice = input("Enter your choice: ")

try:
    math[choice](x,y)

except KeyError:
    print('No function for this value. Please refer to the menu.')

except ValueError:
    print("Enter numbers only.")

except MemoryError:
    print("Oops, ran out of memory.")

else:
    print("Code successfully ran.")

finally:
    print("Good bye!!")
