from time import sleep
from datetime import datetime, date
import builtins
import codecs

class SaveData:
    def __init__(self, name, password, filename): # Stores username, password, and output filename
        self.name = name
        self.password = password
        self.filename = filename


    def setPassword(self): # Changes the user's password in the database
        password = input('What would you like to set your password to? ')
        oldpassword = ":" +self.password
        self.password = password
        password = ":" + password

        #Changes the password in the database
        fin = open("Database.data", "rt")
        data = fin.read()
        oldpassword = codecs.encode(oldpassword, 'rot13')
        password = codecs.encode(password, 'rot13')
        data = data.replace(oldpassword, password)
        fin.close()
        fin = open("Database.data", "wt")
        fin.write(data)
        fin.close()

        self.print('Your password has been changed successfully.')

    def Login(self): # Login module (Uses rot13 encoding to encode user data)
        while True:
            print('Hi, please login by entering your name.')
            username = input('Username: ')
            self.username = username
            with open('Database.data') as f:
                loginlist = f.read()
                f.close()
            with open('Database.data', 'a') as f:
                # Checks login database to see if user has an account
                if loginlist.find(codecs.encode(username+':', 'rot13')) == (-1):
                    password = input("It looks like this is your first time logging in. Please enter a password: ")
                    self.password = password
                    # Appends user login data as new entry to database
                    f.write('\n')
                    userdata = (username+':'+password)
                    f.write(codecs.encode(userdata, 'rot13'))
                    f.close()
                    print('Account created successfully. Welcome,',username+'!')
                    break
                else:
                    password = input('Welcome back, '+username+'! Enter your password to log in: ')
                    # Checks login database to see if username is paired with given password
                    if loginlist.find((codecs.encode(username+':'+password, 'rot13'))) != (-1):
                        self.username = username
                        self.password = password
                        print('Login successful.')
                        break
                    else:
                        print('Login unsuccessful.')
                        print('Try again in 5 seconds.')
                        sleep(5)
                        continue

    def getUsername(self):
        return self.username

    def initiateSaveData(self): # Creates the filename variable to initiate the chat log
        now = datetime.now()
        current_time = now.strftime("%H%M%S")
        filename = self.username + "log" + str(date.today()) + '-' + current_time + '.log'
        self.filename = filename


    def getFileName(self):
        return self.filename


    def print(self, *args, **kwargs): # Appends the text to the file, then prints it as normal
        toprint = ' '.join([str(arg) for arg in args])
        file = open(self.filename, "a", encoding="utf-8")
        file.write(toprint+'\n')
        file.close()
        return builtins.print(*args, **kwargs)

    def input(self, *args, **kwargs): # Appends input to the text file, then returns input as normal
        toprint = ' '.join([str(arg) for arg in args])
        file = open(self.filename, "a", encoding="utf-8")
        file.write(toprint + '\n')
        real_input =  builtins.input(*args, **kwargs)
        file.write(real_input + '\n')
        file.close()
        return real_input