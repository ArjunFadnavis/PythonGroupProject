#
# Authors - Arjun Fadnavis, Theresa Granger, Tiffany Anderson, Alexandre Eldredge
# 07/18/2021
# This function allows users to change their passwords
#

def change_password():
    student_id = input('enter student id: ')
    while student_id not in ['1001', '1002', '1003', '1004']:
        print('invalid ID')
        student_id = input('enter student id: ')
    password = input('enter your password ')
    file = open('passwords', 'r+')
    lines = file.readlines()
    for line in reversed(lines):
        if student_id in line:
            line = line.strip()
            while line != f'{student_id} {password}':
                print('invalid login')
                student_id = input('enter student id: ')
                password = input('enter your password ')
            password = input('enter your new password ')
            while True:
                while len(password) < 8:
                    print('password must be 8 or more characters long')
                    password = input('enter your new password ')
                while password.isupper():
                    print('passwords must have mixed cases')
                    password = input('enter your new password ')
                while password.islower():
                    print('passwords must have mixed cases')
                    password = input('enter your new password ')
                while password.isnumeric():
                    print('passwords must have letters')
                    password = input('enter your new password ')
                while password.isalpha():
                    print('passwords must have numbers')
                    password = input('enter your new password ')
                while password.isalnum():
                    print('passwords must have special characters')
                    password = input('enter your new password ')
                break

            line = f'{student_id} {password} \n'
            file.write(line)
            break

    file.close()
