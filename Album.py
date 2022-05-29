from turtle import position
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



def searchforsongs(albumname):
    file=open("music.txt","r")
    songs=list()
    linenumber=0
    for i in file:
        linenumber+=1
        position=list()
        values=i.split()
        album=values[1]
        if(album==albumname):
            position.append(values[0])
            position.append(linenumber)
            songs.append(position)
    file.close()
    return songs

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
    x=input("Enter the number to play song")
    return x

album=input("Enter the album name:")
while (album!="back"):
    albumname=""
    for i in album:
        if(i==" "):
            albumname+="_"
        else:
            i=i.lower()
            albumname+=i

    songs=searchforsongs(albumname)
    if(songs):
        printsongnames(songs)
        x=songtobeplayed()
        if(x=="back"):
            break
        else:
            file=open("commonfile.txt","a")
            x=int(x)-1
            value="%s"%songs[x][1]
            str=" "+songs[x][0]+" "+value
            file.write(str)
            file.close()
            exec(open("Play.py").read())
        clearConsole()
    else:
        print("Sorry it is not available")
    album=input("Enter the album name:")
clearConsole()
print("Going back...")