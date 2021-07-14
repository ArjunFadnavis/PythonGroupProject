from student import add_course
from student import drop_course
from student import course_list
from billing import display_hours_bill
from billing import calculate_hours_and_bill


def main():
    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    in_state_list = ['1001', '1003']
    course_list = ['CSC101', 'CSC102', 'CSC103', 'CSC104']
    course_hours = [3, 4, 5, 3]
    max_size_list = [3, 2, 1, 3]
    roster_list = [['1004', '1003'], ['1001'], ['1002'], []]

    id = input('enter ID to login or 0 to quit ')
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
                course_list(id, course_list, roster_list)
            elif choice == 4:
                calculate_hours_and_bill(id, in_state_list, r_list, course_hours)
                display_hours_bill(hours, cost)
            else:
                print('session ended')
                quit()
        print('session ended')
        id = input('enter ID to login or 0 to quit ')


# login function
def login(id, student_list):
    file = open('passwords', 'r+')
    while id not in ('1001', '1002', '1003', '1004'):
        print('invalid ID')
        id = input('enter ID ')
    # going backwards to read updated info w/ passwords first
    lines = file.readlines()
    for line in reversed(lines):
        if id in line:
            line = line.strip()
            # has no password
            if line == id:
                while True:
                    try:
                        pin = (input('enter pin '))
                        if (id, pin) not in student_list:
                            raise ()
                    except:
                        print('error invalid login')
                        id = input('enter student id ')
                        while id not in ('1001', '1002', '1003', '1004'):
                            print('invalid ID')
                            id = input('enter ID ')
                    else:
                        # sets password
                        while True:
                            try:
                                password = input('choose a password ')
                                # password strength check
                                if len(password) < 8:
                                    print('password must be 8 or more characters long')
                                    raise ()
                                if password.isupper():
                                    print('passwords must have mixed cases')
                                    raise ()
                                if password.islower():
                                    print('passwords must have mixed cases')
                                    raise ()
                                if password.isnumeric():
                                    print('passwords must have letters')
                                    raise ()
                                if password.isalpha():
                                    print('passwords must have numbers')
                                    raise ()
                                if password.isalnum():
                                    print('passwords must have special characters')
                                    raise ()

                            except:
                                print('except works')
                                continue
                            else:

                                line = f'{id} {password} \n'
                                file.write(line)
                                break
                        break

            else:
                # password is set
                password = input('enter password ')
                if line == f'{id} {password}':
                    print('valid login')
                    break
                else:
                    # incorrect password
                    while line != f'{id} {password}':
                        print('invalid login')
                        id = input('enter student id ')
                        password = input('enter password ')
                    break
    file.close()


# List Course


main()
