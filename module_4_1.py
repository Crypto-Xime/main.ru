# module_4_1.py and Import from other docs

from fake_math import divide as fake_divide
from truth_math import divide as truth_divide

# Assigning Values Source Code (function names):
# Test the functions
result1 = fake_divide(69, 3)    # Should return 23.0
result2 = fake_divide(3, 0)     # Should return "Error"
result3 = truth_divide(49, 7)   # Should return 7.0
result4 = truth_divide(15, 0)   # Should return inf

# Printing The Results fo the Output:

print('*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*')
print(result1)
print(result2)
print(result3)
print(result4)
print('*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*')

