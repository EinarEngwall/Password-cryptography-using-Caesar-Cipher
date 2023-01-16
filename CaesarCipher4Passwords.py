
from pickle import APPEND
import random
import time
import re





alphabet = [
 "a", "b","c", "d", "e", "f", "g", "h", "j", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", 
"y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_", ".", "#", "-","?", "+"
]

new_u_password = ""
    
startq = input("Do you want to read passwords, get new or save another password? \n")

line0 = 0
line1 = 1
line2 = 2
count = 0
if startq == "read":
    with open(r"pw_file", 'r') as fp:
        lines = len(fp.readlines())
        rep = lines / 3


    while count < rep:
        count = count + 1
        with open("pw_file", 'r') as fp:
            line_numbers = [line0,line1,line2]
            lineshift = []
            for i, line in enumerate(fp):
                if i in line_numbers:
                    lineshift.append(line.strip())
        
        for c in lineshift[0]:
            index = alphabet.index(c) 
            c = index - int(lineshift[2])
            if c < 0:
                c = c + 1
            listcha = alphabet[c]
            new_u_password += listcha

        print(new_u_password + " for " + lineshift[1] + "\n")


        new_u_password = ""
        
        line0 += 3 
        line1 += 3 
        line2 += 3 

        line_numbers = [line0,line1,line2]




if startq == "new":
    shift = random.randrange(2,15)


    u_password = input("Enter password: \n")
    u_site = input("Enter website name: \n")


    for c in u_password:
        
        charac_index = alphabet.index(c) 
        c = (int(charac_index) + shift)
        
        if c > len(alphabet):
            c = c - len(alphabet) - 1
        if c == len(alphabet):
            c = c - 1

        listcha = alphabet[c]
        new_u_password += listcha

        with open("pw_file", "w+") as pw:
            pw.write(new_u_password  + "\n")
            pw.write(u_site + "\n")
            pw.write(str(shift) + "\n")
        

if startq == "new":
    startq = input("Do you want to save another password? \n")




if startq == "another":
    while startq == "another":
        u_password = ""
        shift = 0
        new_u_password = ""
        shift = random.randrange(2,15) 
        u_password = input("Enter password: \n")

        u_site = input("Enter website name: \n")

        for c in u_password:
        
            charac_index = alphabet.index(c) 
            c = (int(charac_index) + shift)
        
            if c > len(alphabet):
                c = c - len(alphabet) - 1
            if c == len(alphabet):
                c = c - 1

            listcha = alphabet[c]
            new_u_password += listcha

        with open("pw_file", "a") as pw:
            pw.write(str(new_u_password)  + "\n")
            pw.write(str(u_site) + "\n")
            pw.write(str(shift) + "\n")
        
        startq = input("Do you want to save another password? \n")