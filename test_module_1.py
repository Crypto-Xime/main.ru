# Giving Data as Input
List_Grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
Set_Students = {'Johnny', 'Billy', 'Steve', 'Sheldon', 'Aaron'}

# Creating A List Of Students To Match The Order Of Grades
sorted_students = sorted(Set_Students)

# Create a Dictionary to store GPA For Each Student Shown
gpa_dict = {}

# Calculation GPA and Store It in The Dictionary
for student, List_Grades in zip(sorted_students, List_Grades):
    gpa = sum(List_Grades) / len(List_Grades)
    gpa_dict[student] = gpa

# Print the result Dictionary
print("Students Grades:", gpa_dict)


