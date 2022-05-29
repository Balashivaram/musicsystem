import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def lowerword(word):
    returnword=""
    for i in word:
        if(i==" "):
            returnword+="_"
        else:
            i=i.lower()
            returnword+=i
    return returnword

clearConsole()
x=input("Do you want to enter the song (Y/End)")
x=x.lower()
while(x=="y"):
    songname=input("Enter the song name:")
    songname=lowerword(songname)
    albumname=input("Enter the album name:")
    albumname=lowerword(albumname)
    duration=input("Enter the duration:")
    artistname=input("Enter the artist name:")
    artistname=lowerword(artistname)
    writername=input("Enter the writername:")
    writername=lowerword(writername)
    language=input("Enter the language:")
    language=lowerword(language)
    genre=input("Enter the genre:")
    genre=lowerword(genre)
    total="0"
    str=songname+" "+albumname+" "+duration+" "+artistname+" "+writername+" "+language+" "+genre+" "+total
    file=open("music.txt","a")
    file.write(str+"\n")
    print("Song added Successfully")
    x=input("Do you want to enter the song (Y/End)")
    x=x.lower()
    clearConsole()