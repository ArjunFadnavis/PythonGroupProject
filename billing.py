from Registration import course_list
from Registration import roster_list
from Registration import course_hours


def calculate_hours_and_bill(id, i_s_list, r_list, h_list):
    enrollment_price = 0
    # set tuition prices
    while str(id) in i_s_list:
        cost = 225
    else:
        cost = 850
    while id in 1001:
        enrollment_price = cost * course_hours[0]
    while id in 1002:
        enrollment_price = cost * course_hours[1]
    while id in 1003:
        enrollment_price = cost * course_hours[2]
    while id in 1004:
        enrollment_price = cost * course_hours[3]
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
