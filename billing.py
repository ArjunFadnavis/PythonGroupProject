def calculate_hours_and_bill(id, i_s_list, r_list, h_list):
    enrollment_price = 0
    # set tuition prices
    while str(id) in i_s_list:
        cost = 225
    else:
        cost = 850
    first_course = [i[0] for i in roster_list] # these are lists of the student ids in the class
    second_course = [i[1] for i in roster_list]
    third_course = [i[2] for i in roster_list]
    fourth_course = [i[3] for i in roster_list]
    while id in first_course:
        enrollment_price = cost * course_hours[0]
    while id in second_course:
        enrollment_price = enrollment_price + (cost * course_hours[1])
    while id in third_course:
        enrollment_price = enrollment_price + (cost * course_hours[2])
    while id in fourth_course:
        enrollment_price = enrollment_price + (cost * course_hours[3])
    print("total cost:", enrollment_price)
    print("course hours registered for", enrollment_price / cost)


def display_hours_bill(hours, cost):
    # -----------------------------------------------------------------
    # This function displays the course hours and the cost of enrollment.
    # It has two parameters.
    # hours is the number of course hours.
    # cost is the total cost of enrollment.
    # This function displays the total number of credit hours and total
    # cost of enrollment.
    # -----------------------------------------------------------------
    print('Total number of course hours:', hours)
    print('Total cost of enrollment:', cost)
