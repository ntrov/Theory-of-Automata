import re


def validateEmail(email):

    if re.match(r'[a-zA-Z\d\.-]+@(gmail.com|live.com|hotmail.com|yahoo.com)', email):
        print(email + ' : ' + 'Valid Email')
    else:
        print(email + ' : ' + 'Invalid Email')


def main():
    validateEmail("wajahatraza@gmail.com")
    validateEmail("wajahatraza1234567890@yahoo.com")
    validateEmail("wajahat.raza1234567890@hotmail.com")
    validateEmail("wajahat-raza1234567890@live.com")
    validateEmail(".wajahatraza1234567890@gmail.com")
    validateEmail("-wajahatraza1234567890@gmail.com")
    validateEmail("wajahatraza1234567890-@gmail.com")
    validateEmail("wajahatraza1234567890.@gmail.com")
    validateEmail("w@gmail.com")
    validateEmail("@gmail.com")
    validateEmail("wajahatraza")
    validateEmail("wajahatraza@")
    validateEmail("wajahatraza_@gmail.com")


if __name__ == '__main__':
    main()
