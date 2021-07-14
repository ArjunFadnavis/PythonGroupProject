def calculate_hours_and_bill(id, i_s_list, r_list, h_list):
    enrollment_price = 0
    # set tuition prices
    if str(id) in i_s_list:
        cost = 225
    else:
        cost = 850
    CSC101 = r_list[0] # these are lists of the student ids in the class
    CSC102 = r_list[1]
    CSC103 = r_list[2]
    CSC104 = r_list[3]
    while id in 101:
        enrollment_price = cost * h_list[0]
    while id in 102:
        enrollment_price = enrollment_price + (cost * h_list[1])
    while id in 103:
        enrollment_price = enrollment_price + (cost * h_list[2])
    while id in 100:
        enrollment_price = enrollment_price + (cost * h_list[3])
    print("total cost:", enrollment_price)
    print("course hours registered for", enrollment_price / cost)
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
