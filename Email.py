# make dictionary with emails in it then use Regular Expression to store the data and make the email and password.
import re
import random
import string
emails = "C:/Users/13035/OneDrive/Documents/emails.txt"
p = re.compile("([A-Z]).+_(.+)@(.+)\.yahoo\.com$")
Appended_emails = []
Usernames = {}
Passwords = {}
with open (emails,'r') as e:
    lines = e.readlines()
    for line in lines:
        Appended_emails.append(line.capitalize())

    for email in Appended_emails:
        email = email.strip()
        match = re.search(p, email)
        if match:
            x = random.randint(100000000, 999999999)
            x = str(x)
            z = random.randint(100000000, 999999999)
            z = str(x)
            y = random.randint(0, 9)
            y = str(y)
            name_part = match.group(1)  
            domain_part = match.group(2)
            Department = match.group(3)
            if [name_part+domain_part+"-"+Department] in Usernames:
                Usernames[name_part+domain_part+"2"+"-"+Department] = 1
                Passwords[name_part+domain_part+z] = 1
            else:
                Usernames[name_part+domain_part+"-"+Department] = 1
                Passwords[name_part+domain_part+x] = 1
        else:
            print("No match found: '"+ email + "'")
    print(Usernames)