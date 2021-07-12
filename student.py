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


def list_courses(id, c_list, r_list):
    registered_courses = []
    counted_courses = 0
    for i in range(len(r_list)):
        if id in r_list[i]:
            counted_courses += 1
            registered_courses.append(c_list)
    print('You are currently registered in an total of', counted_courses, 'courses.')
    print('The courses are: ', registered_courses)
