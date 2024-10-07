                              # Problem "It's not that simple"

# Creating Example 1 New List Odd and Even Numbers; Assigned Values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Even_Numbers = []
Odd_Numbers = []

for item in numbers:
    if item % 2 == 0:
        Even_Numbers.append(item)
    else:
        Odd_Numbers.append(item)
print("Even Numbers:",Even_Numbers)
print("Odd Numbers:",Odd_Numbers)

#Creating Example Number 2 New List Odd Numbers and Assigned Values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
i = 0

while i < len(numbers):
    if numbers[i] % 2==1:
        print("Odd Numbers:", numbers[i])
    i += 1

#Creating New List Even Numbers and Assigned Values
for i in numbers:
    if i % 2==1:
        continue
    else:
        print("Even Numbers:", i)
