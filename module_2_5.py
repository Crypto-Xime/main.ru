                                            # "Matrix incarnate"
#EXAMPLE 1
# Define Function and Create an Empty List
def get_matrix( n, m, value):
    matrix = []

# Create Loop Rows
    for i in range(n):
        row = []
        for a in range(m):
            row.append(value)
        matrix.append(row)

    return matrix

# Display Results as Step 6

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)

# EXAMPLE 2
# Define Function and Create an Empty List

def get_matrix(n, m, value):
    matrix = []

    index = 0
    while index < n:
        row = []

    index1 = 0
    while index1 < m:
        row.append(value)
        index1 += 1
    matrix.append(row)
    index += 1

    return matrix

#create empty list

new_matrix1 = get_matrix(2,2,10)
new_matrix2 = get_matrix(3,5,42)
new_matrix3 = get_matrix(4,2,13)

# Exercise

print(new_matrix1)
print(new_matrix2)
print(new_matrix3)




