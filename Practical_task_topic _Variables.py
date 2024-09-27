# display of information

course_name = "Python"
total_tasks = 12
total_hours_spent = 1.5
average_completion_hours = 0.50

# Assigning average completion hours, tasks and hours spent
completion_hours = total_hours_spent / total_tasks
course_name_str = (str(course_name)).lower()
total_tasks_str = (str(total_tasks)).lower()

#print course details
print(f"course name: {course_name_str}")
print(f"total tasks: {total_tasks_str}")
print(f"hours spent: {total_hours_spent}")
print(f"average completion hours: {completion_hours:}")