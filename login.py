student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
lowercase_only = []
uppercase_only = []
nums_only = []
letters_only = []
student_id = input('enter student id ')
file = open('passwords', 'r+')
for line in file:
    if student_id in line:
        line = line.strip()
        if '1002' == line:
            print('ok')
        # has no password
        if line == student_id:
            print('hello')
            while True:
                try:
                    pin = (input('enter pin '))
                    if (student_id, pin) not in student_list:
                        raise ()
                except:
                    print('error invalid login')
                    student_id = input('enter user id ')
                else:
                    # sets password
                    password = input('enter a password ')
        else:
            print('fail')
        #     # password is set
        #     split = line.split()
        #     password = split[1]
        #     if line == f'{student_id} {password}':
        #         print('valid login')
        #         break
    else:
        continue
# def password_c    heck(password):
#     while 0 == 0:
#         for characters in password:
#             if characters.isupper():
#                 uppercase_only.append(characters)
#             elif characters.islower():
#                 lowercase_only.append(characters)
#             elif characters.isnumeric():
#                 nums_only.append(characters)
#             elif characters.isalpha():
#                 letters_only.append(characters)
#         if len(password) < 8:
#             print('password must be 8 or more characters long')
#             password = input('enter your password ')
#             continue
#         elif len(uppercase_only) == len(password):
#             print('passwords must have mixed cases')
#             password = input('enter your password ')
#             continue
#         elif len(lowercase_only) == len(password):
#             print('passwords must have mixed cases')
#             password = input('enter your password ')
#             continue
#         elif len(nums_only) == len(password):
#             print('passwords must have letters')
#             password = input('enter your password ')
#             continue
#         elif len(letters_only) == len(password):
#             print('passwords must have numbers')
#             password = input('enter your password ')
#             continue
#         elif password.isalnum():
#             print('passwords must have special characters')
#             password = input('enter your password ')
#         else:
#             break
# This is a test - Jmatlock
# This is a test - Jmatlock
# This is another test
# This is yet another test
#merge conflict test
# merge conflict from jmatlock

