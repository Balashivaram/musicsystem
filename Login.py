file=open("login.txt","r")
file1=open("commonfile.txt","w")
username=input("Enter the username:")
password=input("Enter the password:")
flag=1
if username=="root" and password=="password":
    print("Welcome back root")
    exec(open("root.py").read())
    file1.write("2")
else:
    for i in file:
        if username in i:
            if password in i:

                print("Login Successful...")
                flag=0
                file1.write("1")
                file1.write(" "+username)
                break

    if(flag):
        print("Login Unsuccessful...")
        file1.write("0")

