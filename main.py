def print_hello(name):
    print(f'Hello, {name}')
if __name__ == '__main__':
    'PyCharm'

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def print_hello(name):
    print(f'Hello, {name}')
if __name__ == '__main__':
        print_hello('World!')

#1st program
print(9**0.5*5)

#2nd program
print(9.99>9.98) and (1000==1000.1)

#3rd program
print((2**2)+2)
print((2+2)**2)
print(((2**2)+2) == ((2+2)**2))

#4th program
print(type(123.456))

                     #Decimal to Fraction

from fractions import Fraction

           #define the decimal number
decimal_number = 123.456

           #Convert to fraction
fraction = Fraction(decimal_number).limit_denominator()

           #Print the result
print(f"Fraction representation: {fraction}")

                     #Shift . a space
print(10*123.456)

                     #Result of the division between large Fraction and an integer Simplifying it

from fractions import Fraction

            #define the fraction
numerator = 15432
denominator = 125
fraction = Fraction(numerator, denominator)

            #Simplify the fraction (automatically done)
simplified_fraction = fraction

            #Define the integer to divide by
integer = 10

            #divide the simplified fraction by the integer
result = simplified_fraction / integer

            #Print the result
print(f"Simplified fraction: {simplified_fraction}")
print(f"Result of division: {result}")

print(int(float('123.456')*10%10))

