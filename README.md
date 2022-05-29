# Music System
Createed a Terminal App in Python for Microsoft Engage 2022


It consists of **12 files**.They are 


  - main.py
  - login.py
  - Signup.py
  - Recomends.py
  - Song.py
  - Artist.py
  - Album.py
  - Play.py
  - commonfile.txt
  - login.txt
  - music.txt
  - Root.py

# Working Of Each File

## main.py

We are going to run this file in terminal and then it will ask user whether they have an account or not if user press Y it will open login.py and if user 
presses N it will open Signup.py and then it will go to the commonfile.txt and then reads a number that is either 1 or 0 if it is 1 it is a condition that user logged in successfully or he created a account and it will display a menu that has 
''' 

>1)Recomend Songs <br>
2)Search for an album <br>
3)Search for a song <br>
4)Search for an artist <br>
Enter an option: <br>


If user press 1 it will open Recomend.py if user presses 2 it will open Album.py if user presses 3 it will open Song.py if user persses 4 it will open
artist.py if user types end it will stop running the application

## login.py

It will ask user to type their username and then their password and then it will open login.txt file in read mode and then it will check for the user 
typed username and psasword and then if it is there it will *** Login Successful... *** and then it iwll open ** commonfile.txt ** in write mode and then 
it will wirte 1 to the file it is to inform that login is successful to main.py if username and password and not found it will print *** Login unsuccessful... *** and then it will write 0 to the ** commonfile.txt ** 0 indicates that login was unsuccessful

## Signup.py

It is used to create account in the applciation and then it will get the user informations such as 
> - Name
  - Username
  - Password
  - Country
  - Genre
  - Artist
  - Language <br>
  
It will store these information in ** login.txt ** file and then it wil open ** commonfie.txt ** and then it will write 1 to the file to indicate that the account was created successfully and then it will not allow two users to have same username. If a user types a username that already oher user has it will print a error message.

## Recomends.py
