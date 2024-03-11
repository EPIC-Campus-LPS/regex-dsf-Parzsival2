# make dictionary with emails in it then use Regular Expression to store the data and make the email and password.
import re
import string
re.findall
emails = 'emails.txt'
with open (emails,'r') as e:
    lines = e.readlines()
    for line in lines:
        lines.append(line.capitalize())

    #user = lines.search(r"([A-Z])[.+]_(.+)@(.+)[.yahoo.com]$")
    print(lines)
