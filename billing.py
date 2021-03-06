# 
# Authors: Arjun Fadnavis, Alexandre Eldredge, Tiffany Anderson, Theresa Granger
# Date: July 18th, 2021
#
# The billing module calculates the hours and classes 
# For each student and then returns the cost of enrollement
# And hours enrolled in


def calculate_hours_and_bill(id, i_s_list, r_list, h_list):
    # -----------------------------------------------------------------
    # This function calculates the course hours and cost of enrollment.  It has five parameters: 
    #   •	i_s_list is the list of in state students
    #   •	r_list is the list of class rosters
    #   •	h_list is the credit hours of each class 
    #This function calculates the bill based on $225 per credit hour for 
    # in-state students and $850 per credit hour for out-of-state students. 
    # After calculating the bill, the function returns the total number of 
    # credit hours and the total cost of enrollment.
    # -----------------------------------------------------------------
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
        enrollment_price = cost * h_list[0]
    if id in CSC102:
        enrollment_price = enrollment_price + (cost * h_list[1])
    if id in CSC103:
        enrollment_price = enrollment_price + (cost * h_list[2])
    if id in CSC104:
        enrollment_price = enrollment_price + (cost * h_list[3])
    hours = enrollment_price / cost
    return hours, enrollment_price


def display_hours_and_bill(hours, cost):
    # -----------------------------------------------------------------
    # This function displays the course hours and the cost of enrollment.
    # It has two parameters.
    # hours is the number of course hours.
    # cost is the total cost of enrollment.
    # This function displays the total number of credit hours and total
    # cost of enrollment.
    # -----------------------------------------------------------------
    print('Total number of course hours: %d' % hours)
    print(f'Total cost of enrollment: ${cost}')
