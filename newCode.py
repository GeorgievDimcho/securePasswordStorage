import hashlib  # used for the pbkdf2 function
import os  # used for generating random bytes = salt and working with files
# import getpass # invisible passwort entry

users = {}  # username, salt and hash value from the password are stored here


def register():
    # add user
    print("new username: ")
    username = input()
    print("new password: ")
    password = input()
    # password = getpass.getpass("User Name : %s" % username)
    # print(password)

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
    FileOutput = [username, users[username], "°"]
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
    # print("users(user)")
    # print(users[enteredUsername])
    # print("user salt: ")
    currentUser = users[enteredUsername]
    # print(currentUser['salt'])
    if users.keys().__contains__(enteredUsername):
        # print("user found")
        enteredKey = hashlib.pbkdf2_hmac('sha512', enteredPassword.encode('utf-8'), bytes.fromhex(currentUser['salt']), 310000, 1024).hex()
        # print("hashed password: " + enteredKey)
        if currentUser['key'] == enteredKey:
            print("Authentication succesful!")
        else:
            print("Wrong password!")
    else:
        print("user not found")


def main():
    while True:
        print("press (r) for register, (l) for log in or (e) for exit: ")
        choice = input()
        if choice == "r":
            register()
        else:
            if choice == "l":
                login()
            else:
                if choice == "e":
                    print("see you around")
                    break
                else:
                    print("invalid input. try again")


def loadDataFromFile():
    try:
        file = open("Password.secure")
    except:
        print("Data could not be imported!")
    else:
        user = []
        for x in file:
            user.append(x.split('°'))
        # print("list: ")
        # print(user)
        salt = ""
        saltIndex = str(user).find("salt")
        # print(saltIndex)
        keyIndex = str(user).find("key")
        # print(keyIndex)
        salt = str(user)[int(saltIndex+8):int(keyIndex-4)]
        print(salt)
        key = ""
        # for y in user:
        #     for c in y:

        # print(data)
        # print("users: ")
        # print(users.values())


if __name__ == "__main__":
    loadDataFromFile()
    main()
