from nick import create_nick

with open('users.csv') as userfile:
    # read the lines
    for row in userfile.readlines():
        user = row.strip().split(',')

        firstname = user[0]
        lastname = user [1]

        nickname = create_nick(firstname, lastname)

        print nickname

