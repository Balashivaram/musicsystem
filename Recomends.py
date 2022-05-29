import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)



def searchmusic(type,number):
    lists=type.split(",")
    linenumber=list()
    songs=list()
    file=open("music.txt","r")
    for i in lists:
        total=1
        for j in file:
            music=j.split()
            musictype=music[number]
            if(i==musictype):
                linenumber.append(total)
                songs.append(music[0])
            total+=1
    return songs,linenumber
        
def upperword(song):
    songname=""
    for i in song:
        if(i=="_"):
            songname+=" "
        else:
            songname+=i
    songname=songname.capitalize()
    return songname

def printsongs(songs):
    count=1
    for i in songs:
        songname=upperword(i)
        print("%s"%count+")"+songname)
        count+=1


print("Songs recpmended for you:")
file=open("commonfile.txt","r")
for i in file:
    lists=i.split()
    username=lists[1]
file.close()
file1=open("login.txt","r")
for i in file1:
    lists=i.split()
    if(username==lists[1]):
        break

n=random.randint(0,2)

if(n==0):
    number=6
    songs,linenumber=searchmusic(lists[4],number)
    printsongs(songs)
    file2=open("commonfile.txt","a")
    x=input("Enter the number to play the song:")
    if(x!="back"):
        x=int(x)
        value="%s"%linenumber[x-1]
        file2.write(" "+value)
        file2.close()
        exec(open("Play.py").read())
    print(linenumber)

if(n==1):
    number=3
    songs,linenumber=searchmusic(lists[5],number)
    printsongs(songs)
    file2=open("commonfile.txt","a")
    x=input("Enter the number to play the song:")
    if(x!="back"):
        x=int(x)
        value="%s"%linenumber[x-1]
        file2.write(" "+value)
        file2.close()
        exec(open("Play.py").read())
if(n==2):
    number=5
    songs,linenumber=searchmusic(lists[6],number)
    printsongs(songs)
    file2=open("commonfile.txt","a")
    x=input("Enter the number to play the song:")
    if(x!="back"):
        x=int(x)
        value="%s"%linenumber[x-1]
        file2.write(" "+value)
        file2.close()
        exec(open("Play.py").read())

print("Going back!!!")
clearConsole()
