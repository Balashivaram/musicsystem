def checkusername(username):
    file=open("login.txt","r")
    for i in file:
        lists=i.split()
        if(username==lists[1]):
            flag=1
            print("Username already taken :(")
            print("Try different username :)")
            return flag
        else:
            flag=0
            return flag

def lowerword(word):
    returnword=""
    for i in word:
        if(i==" "):
            returnword+="_"
        elif(i==","):
            returnword+=","
        else:
            i=i.lower()
            returnword+=i
    return returnword


print("Note:If you are giving more than two input seperate with comma")
file=open("login.txt","a")
file1=open("commonfile.txt","w")
name=input("Name:")
n=name
name=""
for i in n:
    if(i==" "):
        name+="_"
    else:
        name+=i
flag=1
while(flag):
    username=input("Enter username:")
    flag=checkusername(username)
password=input("Password:")
country=input("Enter country name:")
genre=input("Genre:")
genre=lowerword(genre)
artist=input("Artist:")
artist=lowerword(artist)
language=input("Language:")
language=lowerword(language)
str=name+" "+username+" "+password+" "+country+" "+genre+" "+artist+" "+language
file.write(str+"\n")
file1.write("1")
file1.write(" "+username)
file1.close()