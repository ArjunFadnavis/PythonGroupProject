def main():
    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    in_state_list = ['1001', '1003']
    course_list = ['CSC101', 'CSC102', 'CSC103', 'CSC104']
    course_hours = [3, 4, 5, 3]
    max_size_list = [3, 2, 1, 3]
    roster_list = [['1004', '1003'], ['1001'], ['1002'], []]
    lowercase_only = []
    uppercase_only = []
    nums_only = []
    letters_only = []
    login()
    choice = int(input('Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: '))
    while choice != 0:
        if choice == 1:
            add_course(id, course_list, roster_list, max_size_list)
            choice = int(
                input('Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: '))
        elif choice == 2:
            drop_course(id, course_list, roster_list)
            choice = int(input('Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: '))
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            quit()


def add_course(id, c_list, r_list, m_list):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has four
    # parameters: id is the ID of the student to be added; c_list
    # is the course list; r_list is the list of class rosters;
    # m_list is the list of maximum class sizes.  This function
    # asks user to enter the course he/she wants to add.  If the
    # course is not offered, display error message and stop.
    # If the course is full, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.  Add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------
    idstring = str(id)
    course_choice = input('Enter course you want to add: ')
    if course_choice in c_list:
        print('Course: ', course_choice)
        course_index = int(c_list.index(course_choice))
        rostercheck = r_list[course_index]
        print('Rostercheck: ', rostercheck)
        maxcheck = m_list[course_index]
        print('Max Cap check: ', maxcheck)
        for course in c_list:
            if str(id) in rostercheck:
                print('Error, you are already enrolled')
                break
            elif len(rostercheck) >= maxcheck:
                print('Error, max capacity')
                break
            else:
                print('Course added')
                r_list[course_index].append(idstring)
                print('Updated roster:', r_list)
                break
    else:
        print('Error: Course not found')


# removes courses
def drop_course(id, c_list, r_list):
    course = input('enter course you want to drop: ')
    course = course.upper()
    if course in c_list:
        course_index = int(c_list.index(course))
        if id in r_list[course_index]:
            r_list[course_index].remove(id)
            print('updated roster:', r_list)
        else:
            print('student not enrolled')
    else:
        print('course dose not exist')
    # pass # temporarily avoid empty function definition

    # login function

def login():
    student_id = input('enter student id ')
    file = open('passwords', 'r+')
    for line in file:
        if student_id in line:
            line = line.strip()
            # has no password
            if line == student_id:
                while True:
                    try:
                        pin = (input('enter pin '))
                        if (student_id, pin) not in student_list:
                            raise ()
                    except:
                        print('error invalid login')
                        student_id = input('enter student id ')
                    else:
                        # sets password
                        while True:
                            try:
                                password = input('enter a password ')
                                # password strength check
                                for characters in password:
                                    if characters.isupper():
                                        uppercase_only.append(characters)
                                    if characters.islower():
                                        lowercase_only.append(characters)
                                    if characters.isnumeric():
                                        nums_only.append(characters)
                                    if characters.isalpha():
                                        letters_only.append(characters)
                                    if len(password) < 8:
                                        print('password must be 8 or more characters long')
                                        raise ()
                                    elif len(uppercase_only) == len(password):
                                        print('passwords must have mixed cases')
                                        print('jello')
                                    elif len(lowercase_only) == len(password):
                                        print('passwords must have mixed cases')
                                        raise ()
                                    elif len(nums_only) == len(password):
                                        print('passwords must have letters')
                                        raise ()
                                    elif len(letters_only) == len(password):
                                        print('passwords must have numbers')
                                        raise ()
                                    elif password.isalnum():
                                        print('passwords must have special characters')
                                        raise ()

                            except:
                                continue
                            else:
                                line = student_id + ' ' + password
                                file.write(line)
                                break
                        break

            else:
                # password is set
                password = input('enter password ')
                if line == f'{student_id} {password}':
                    print('valid login')
                    break
                else:
                    # incorrect password
                    while line != f'{student_id} {password}':
                        print('invalid login')
                        student_id = int(input('enter student id '))
                        password = input('enter password ')
    file.close()


main()
