# password = genorated password
# usernameanswer = the username submitted by the user
# emailanswer = email submitted by the user
# passask = asks wether or not the user would like a password genorated, or if they have their own
# userpass = the password submitted by the user if they choose to use their own
# appanswer = the site/app that the information is for

from pyfiglet import figlet_format
import random
import keyboard

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
symbols = '!#$.*()/?'

length = 12

userpass = ""

nothing = ""

string = uppercase_letters + lowercase_letters + digits + symbols

password = "".join(random.sample(string,length))

repeatask = True

art = r"""

  _    _             _           _        _____                                    _    _______          _ 
 | |  | |           | |         ( )      |  __ \                                  | |  |__   __|        | |
 | |__| |_   _  __ _| |__  _   _|/ ___   | |__) |_ _ ___ _____      _____  _ __ __| |     | | ___   ___ | |
 |  __  | | | |/ _` | '_ \| | | | / __|  |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |     | |/ _ \ / _ \| |
 | |  | | |_| | (_| | | | | |_| | \__ \  | |  | (_| \__ \__ \\ V  V / (_) | | | (_| |     | | (_) | (_) | |
 |_|  |_|\__,_|\__, |_| |_|\__, | |___/  |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|     |_|\___/ \___/|_|
                __/ |       __/ |                                                                          
               |___/       |___/                                                                           

"""
print(art)

def header():
    print( figlet_format("Hughy's  Password  Logger" , font = "Standard" , width = 300))

# want to use the cool text but it messes with exe, if find fix just add header() below to print it

while repeatask is True:
    #Ask for app/website
    print('What Website/App Is This Information For?')
    appanswer = input('')

    #space
    print('-------------------------------------------------------------------------------------------------')
    #Ask for email
    print('What Is The Email?')
    emailanswer = input('')

    #space
    print('-------------------------------------------------------------------------------------------------')

    #Ask for username
    print('What Is The Username?')
    usernameanswer = input('')

    # space
    print('-------------------------------------------------------------------------------------------------')

    #Ask wether they want a password generated or not
    print('Would You Like A Password Generated For You? | Type 1 For Yes | Type 2 For No')
    passask = int(input(''))

    # space
    print('-------------------------------------------------------------------------------------------------')
    # print password
    if passask == 1:
      nothing
    else:
      print('Ok! Please Enter Desired Password!')
      userpass = input('')
      print('-------------------------------------------------------------------------------------------------')

    infoownpass = appanswer + " Login Information:\n\nEmail: " + emailanswer + "\nUsername: " + usernameanswer + "\nPassword: " + userpass

    infogenpass = appanswer + " Login Information:\n\nEmail: " + emailanswer + "\nUsername: " + usernameanswer + "\nPassword: " + password

    if passask == 1:
      print(infogenpass)
      with open(appanswer + '.txt','w') as file:
        file.write(infogenpass)
        
    else:
      print(infoownpass)
      with open(appanswer + '.txt','w') as file:
        file.write(infoownpass)
              
    print('-------------------------------------------------------------------------------------------------')

    # ask the user wether they want to enter another login info or exit the terminal
    print('Information Saved | Type 1 To Enter More Information | Type 2 to Exit The Program')
    anotherlog = int(input(''))

    print('-------------------------------------------------------------------------------------------------')

    if anotherlog == 1:
      repeatask = True
    elif anotherlog == 2:
      repeatask = False
    
    if anotherlog is False:
      exit()
 
  
    




