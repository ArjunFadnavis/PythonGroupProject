def change_password():
    student_id = input('enter student id: ')
    password = input('enter your password ')
    file = open('passwords', 'r+')
    lines = file.readlines()
    for line in lines:
        

