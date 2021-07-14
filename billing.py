from Registration import course_list
from Registration import roster_list
from Registration import course_hours


def calculate_hours_and_bill(id, i_s_list, r_list, h_list):
    enrollment_price = 0
    # set tuition prices
    if str(id) in i_s_list:
        cost = 225
    else:
        cost = 850
    CSC101 = r_list[0]  # these are lists of the student ids in the class
    CSC102 = r_list[1]
    CSC103 = r_list[2]
    CSC104 = r_list[3]
    if id in CSC101:
        enrollment_price = cost * course_hours[0]
    if id in CSC102:
        enrollment_price = enrollment_price + (cost * h_list[1])
    if id in CSC103:
        enrollment_price = enrollment_price + (cost * h_list[2])
    if id in CSC104:
        enrollment_price = enrollment_price + (cost * h_list[3])
    hours = enrollment_price / cost
    return hours, enrollment_price
    
    
    # need to just return the values to the display_hours_bill function
    # where they will then be printed out


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
