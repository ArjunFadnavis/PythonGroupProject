student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
lowercase_only = []
uppercase_only = []
nums_only = []
letters_only = []


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
                                break
                        break

            else:
                # password is set
                split = line.split()
                password = split[1]
                if line == f'{student_id} {password}':
                    print('valid login')
                    break
                else:
                    # incorrect password
                    while line != f'{student_id} {password}':
                        print('invalid login')
                        student_id = int(input('enter student id'))
                        password = input('enter student ID')
    file.close()
