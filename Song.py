from turtle import position
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def searchforsong(songname):
    file=open("music.txt","r")
    linenumber=0
    for i in file:
        linenumber+=1
        values=i.split()
        song=values[0]
        if(song==songname):
            file1=open("commonfile.txt","a")
            s="%s"%(linenumber)
            file1.write(" "+s)
            file1.close()
            file.close()
            return 1
    return 0

def printsongnames(songs):
    total=1
    for j in songs:
        songname=""
        song=j[0]
        for i in song:
            if(i=="_"):
                songname+=" "
            else:
                songname+=i
        songname=songname.capitalize()
        print("{}){}".format(total,songname))
        total+=1

def songtobeplayed():
    x=input("Do you want to play the song(1)")
    return x

song=input("Enter the song name:")
while(song!="back"):
    songname=""
    for i in song:
        if(i==" "):
            songname+="_"
        else:
            i=i.lower()
            songname+=i

    flag=searchforsong(songname)
    if(flag):
        print("The song you searched is available in database")
        x=songtobeplayed()
        if(x=="back"):
            break
        else:
            exec(open("Play.py").read())
    else:
        print("Sorry we cannot find the song")
        print("Try searching another song")
    song=input("Enter the song name:")
clearConsole()
print("Going Back....")
