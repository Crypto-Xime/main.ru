def print_hello(name):
    print(f'Hello, {name}')
if __name__ == '__main__':
        print_hello('Teacher!')

        # variable string, concatenate and condition

def display_person_info(name , current_age , is_student):
    new_age = current_age + 2
    is_student_str = (str(is_student)).lower()

    info = f"Name: {name}\nAge: {current_age}\nNew age: {new_age}\nIs Student: {is_student_str}"
    return info

#example usage

person_name = "Ximena"
person_age = 26
student_status = True

#Display

print(display_person_info(person_name , person_age ,student_status))
