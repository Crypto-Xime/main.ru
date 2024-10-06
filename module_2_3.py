                                    # Problem Zeros are nothing, denial is unacceptable!

# Assigned Variables Original List, Initial Data
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

for i in my_list:
    if i <= 0:
        continue
    else:
         print (i)

# Example Number 2, Assigned Variables Original List, Initial Data
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0

while i < len(my_list):
    if my_list[i] > 0:
        print(my_list[i])
    i += 1

# Example Number 3, Assigned Variables Original List

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
        if my_list[index] > 0:
         print(my_list[index])
        index += 1
