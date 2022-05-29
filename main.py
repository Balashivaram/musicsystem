import os
import sys

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def mainpage():
    x=input("Do you have an account(Y/N):")
    return x


def signin(x):
    if(x=="y"):
        exec(open("Login.py").read())
    else:
        exec(open("Signup.py").read())

def firstpage():
    print("1)Recomend Songs")
    print("2)Search for an album")
    print("3)Search for a song")
    print("4)Search for an artist")
    x=input("Enter an option:")
    return x;

clearConsole()
print("\t\tMusic System")
flag=0
count=0
while(flag!=1 and count<10):
    count+=1
    x=mainpage()
    x=x.lower()
    signin(x)
    file=open("commonfile.txt","r")
    lines=file.read()
    lines=lines.split()
    flag=int(lines[0])
    if(flag==2):
        sys.exit("Byee Root User!!!")
        break
   
if(flag):
    clearConsole()
    option=firstpage()
    while(option!="end"):
        option=int(option)
        if(option==1):
            clearConsole()
            exec(open("Recomends.py").read())
        elif(option==2):
            clearConsole()
            exec(open("Album.py").read())
        elif(option==3):
            clearConsole()
            exec(open("Song.py").read())
        elif(option==4):
            clearConsole()
            exec(open("Artist.py").read())
        option=firstpage()
    clearConsole()
    print("Ending the music system")
    print("Have a good day!!!")
else:
    print("Sorry ending the music system!!!")
