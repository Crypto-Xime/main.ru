# Exercises Module 3.2

def print_params(a: int = 4,
                 b: int = 8,
                 c: int =10):
    print(a, b, c)
    print(a + c)

print_params(8, True, 14)

def func_with_params(a = 6,
                     b = 10,
                     c = None):
    if c is None:
     c = [a]
    print(c)
    print(a + b)
func_with_params()
func_with_params()


                                            # Mailing of letters
# Defining Sender and types of domains
print()
sender_email = input("Sender Email Address:")
recipient_email = input("Receiver Email Address:")
print("-------------------------------------------------------------------")
subject = input("Subject:")
print("-------------------------------------------------------------------")

Message = input("Message:")

# Function to validate email
valid_domains = [".com", ".ru", ".net"]
is_valid_sender = False
is_valid_recipient = False

# Check if the Sender's Email is Valid
if "@" in sender_email:
    for domain in valid_domains:
        if sender_email.endswith(domain):
            is_valid_sender = True
            break

# Check if the Recipient's Email is Valid or The Same
if "@" in recipient_email:
    for domain in valid_domains:
        if recipient_email.endswith(domain):
            is_valid_recipient = True
            break

# Check Validity and Display Appropriate Messages
if not is_valid_sender or not is_valid_recipient:
    print()
    print("Value Error: Please enter a valid Domain as the address of the recipient.")
    print(" Unable to send a letter from the address {sender} to the address {recipient}.")

else:
    if sender_email == recipient_email:
        print("You can't send a letter to yourself!"
              "Please try again")

    else:
        if sender_email == "university.help@gmail.com" or valid_domains:
            print(f"The letter was successfully sent from the address {sender_email} to the address {recipient_email}.")

        else:
            print(f"NON-STANDARD SENDER! Letter sent from address {sender_email} to the address {recipient_email}.")

