                                             # "Basic Operators"
# Quest Cipher too old:
print()
print("Welcome to Indiana Jones Adventures")
print('-*--*--*--*--*--*--*--*--*--*--*--*-')

def generate_password(num):
     password = ""

     # Create Loop Row and generate unique pairs
     pairs = []
     for i in range(1, 21):
         for a in range(i, 21):
             pairs.append((i, a))

         # Multiples of the pairs
         for (a, b) in pairs:
             pair_sum = a + b
             if num % pair_sum == 0:
                 password += f"{i}{a}"

             return password

# Main Code for the Generated Password
while True:
    try:
        print()
        n = int(input("Enter a number between 3 and 20 or (0 to exit):"))
        if n == 0:
            break

        if 3 <= n <= 20:
                result = generate_password(n)
                if result:
                    print()
                    print(f"The required Password for {n} is {result} ")
                    print("Congratulations Travelers, you have successfully unlocked the gate to freedom!!")
                else:
                    print()
                    print("Value error: No valid password could be generated for that number")
                    print()
        else:
            print("Please enter a valid number between 3 and 20.")

    except ValueError:
                    print("Invalid input. Please enter a valid number between 3 and 20.")