# password = genorated password
# usernameanswer = the username submitted by the user
# emailanswer = email submitted by the user
# passask = asks wether or not the user would like a password genorated, or if they have their own
# userpass = the password submitted by the user if they choose to use their own
# appanswer = the site/app that the information is for

import random

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
symbols = '!#$.*()/?'

length = 12

string = uppercase_letters + lowercase_letters + digits + symbols

password = "".join(random.sample(string,length))

#Ask for app/website
print('What Website/App Is This Information For?')
appanswer = input('')

#space
print('')

#Ask for email
print('What Is The Email?')
emailanswer = input('')

#space
print('')

#Ask for username
print('What Is The Username?')
usernameanswer = input('')

# space
print('')

#Ask wether they want a password generated or not
print('Would You Like A Password Generated For You? 1=YES 2=NO')
passask = int(input(''))

# space
print('')

# print password
if passask == 1:
   print('Ok! Password Genorated!')
   print('')
   print(password)
else:
   print('Ok! Please Enter Desired Password!')
   userpass = input('')
   print('')

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




