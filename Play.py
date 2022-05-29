import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def fetchingsongline():
    file=open("commonfile.txt","r")
    for i in file:
        lists=i.split()
        linenumber=int(lists[len(lists)-1])
        return linenumber


def printsongdetails(word,total):
    w=""
    for i in word:
        if(i=="_"):
            w+=" "
        else:
            w+=i
    w=w.capitalize()
    if(total==0):
        print("Song Name:"+w)
    elif(total==1):
        print("Album:"+w)
    elif(total==2):
        print("Length:"+w)
    elif(total==3):
        print("Composer:"+w)
    elif(total==4):
        print("Lyricist:"+w)
    elif(total==5):
        print("Language:"+w)


def songdetails(line):
    file=open("music.txt","r")
    currentline=1
    for i in file:
        if(currentline==line):
            lists=i.split()
            break
        currentline+=1
    total=0
    for i in lists:
        printsongdetails(i,total)
        total+=1
    file.close()


def modifymusicfile(linenumber):
    file=open("music.txt","r")
    data=file.readlines()
    line=data[linenumber-1]
    line=line.split()
    total=len(line)
    value=int(line[total-1])+1
    value="%s"%value
    line[total-1]=value
    l=""
    for i in line:
        l+=i
        l+=" "
    l+="\n"
    data[linenumber-1]=l
    file.close()
    file=open("music.txt","w")
    file.writelines(data)
    file.close()

def options():
    print("1)Play the song")
    print("2)Go back")
    x=int(input("Enter any one of the option:"))
    return x

def option():
    print("1)Finished Playing the song.Do you want to play again?")
    print("2)Go back")
    x=int(input("Enter any one of the option:"))
    return x

clearConsole()
print("\t\tSong Details")
linenumber=fetchingsongline()
songdetails(linenumber)
x=options()
while(x!=2):
    modifymusicfile(linenumber)
    print("Finished Playint the Song!!!")
    clearConsole()
    songdetails(linenumber)
    x=option()

clearConsole()
print("Going Back....")