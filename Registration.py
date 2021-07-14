from student import add_course
from student import drop_course
from student import list_courses
from billing import display_hours_and_bill
from billing import calculate_hours_and_bill


def main():
    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    in_state_list = ['1001', '1003']
    course_list = ['CSC101', 'CSC102', 'CSC103', 'CSC104']
    course_hours = [3, 4, 5, 3]
    max_size_list = [3, 2, 1, 3]
    roster_list = [['1004', '1003'], ['1001'], ['1002'], []]

    id = input('Enter ID to login or 0 to quit: ')
    while id != '0':
        login(id, student_list)
        choice = int(input('Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: '))
        while choice != 0:
            if choice == 1:
                add_course(id, course_list, roster_list, max_size_list)
                choice = int(
                    input('Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: '))
            elif choice == 2:
                drop_course(id, course_list, roster_list)
                choice = int(
                    input('Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: '))
            elif choice == 3:
                list_courses(id, course_list, roster_list)
                choice = int(
                    input('Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: '))
            elif choice == 4:
                calculate_hours_and_bill(id, in_state_list, roster_list, course_hours)
                hours, enrollment_price = calculate_hours_and_bill(id, in_state_list, roster_list, course_hours)
                display_hours_and_bill(hours, enrollment_price)
                choice = int(
                    input('Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: '))
            else:
                print('Session ended')
                quit()
        print('Session ended')
        id = input('Enter ID to login or 0 to quit: ')


# login function
def login(id, student_list):
    file = open('passwords', 'r+')
    while id not in ('1001', '1002', '1003', '1004'):
        print('Invalid ID')
        id = input('Enter ID ')
    # going backwards to read updated info w/ passwords first
    lines = file.readlines()
    for line in reversed(lines):
        if id in line:
            line = line.strip()
            # has no password
            if line == id:
                while True:
                    try:
                        pin = (input('Enter pin: '))
                        if (id, pin) not in student_list:
                            raise ()
                    except:
                        print('Error invalid login')
                        id = input('Enter student ID: ')
                        while id not in ('1001', '1002', '1003', '1004'):
                            print('Invalid ID')
                            id = input('Enter ID: ')
                    else:
                        # sets password
                        while True:
                            try:
                                password = input('Choose a password: ')
                                # password strength check
                                if len(password) < 8:
                                    print('Password must be 8 or more characters long')
                                    raise ()
                                if password.isupper():
                                    print('Passwords must have mixed cases')
                                    raise ()
                                if password.islower():
                                    print('Passwords must have mixed cases')
                                    raise ()
                                if password.isnumeric():
                                    print('Passwords must have letters')
                                    raise ()
                                if password.isalpha():
                                    print('Passwords must have numbers')
                                    raise ()
                                if password.isalnum():
                                    print('Passwords must have special characters')
                                    raise ()

                            except:
                                print('Except works')
                                continue
                            else:

                                line = f'{id} {password} \n'
                                file.write(line)
                                break
                        break

            else:
                # password is set
                password = input('Enter password: ')
                if line == f'{id} {password}':
                    print('Valid login!')
                    break
                else:
                    # incorrect password
                    while line != f'{id} {password}':
                        print('Invalid login')
                        id = input('Enter student ID: ')
                        password = input('Enter password: ')
                    break
    file.close()


# List Course


main()
