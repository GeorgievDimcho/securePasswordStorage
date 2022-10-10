import hashlib  # used for the pbkdf2 function
import os  # used for generating random bytes = salt and working with files

users = {}  # username, salt and hash value from the password are stored here


def register():
    # add user
    print("create username: ")
    username = input()
    print("create password: ")
    password = input()

    salt = os.urandom(128)  # new salt for this user, size in bytes
    key = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 310000, 1024)
    # (hash_name, password, salt, iterations, dklen) dklen is the length of the derived key. default length of hash alg
    users[username] = {  # store the salt and key
        'salt': salt.hex(),
        'key': key.hex()
    }
    # print(users.get(username))
    # print(salt.hex())
    # print(key.hex())
    # print(users)
    file1 = open("Password.secure", "a")
    FileOutput = [username, str(users.get(username)), "°"]
    file1.writelines(str(FileOutput))
    file1.close()
    print("registration successful")
    # print("salt: " + str(salt))
    # print("hash:" + str(key))


def login():
    print("Enter username: ")
    enteredUsername = input()
    print("Enter password: ")
    enteredPassword = input()
    # print(users.values())
    # print(users.get(1)) None
    # print(users.get(username))
    # print(users.keys()) root

    if users.keys().__contains__(enteredUsername):
        #print("user found")
        enteredKey = hashlib.pbkdf2_hmac('sha512', enteredPassword.encode('utf-8'), users.values(), 310000, 1024).hex()
        print("hashed password: " + enteredKey)
    else:
        print("user not found")
    # create hash and compare


def main():
    while True:
        file = open("Password.secure")
        my_list = []
        for x in file:
            my_list.append(x.split('°'))

        # print(my_list)
        # users
        # print("users: " + users)
        print("press (r) for register and (l) for log in: ")
        choice = input()
        if choice == "r":
            register()
        else:
            if choice == "l":
                login()
            else:
                print("invalid input. try again")


if __name__ == "__main__":
    main()
