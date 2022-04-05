"""
Let's say; you left a message in the past that prints a password you need. To see the password you wrote, you need to enter your name and the program should recognize you. Write a program that  Takes the first name from the user and compares it to yours, Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12", If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later."
"""

a = {
    "name" : "Tolga",
    "password" : 12345
}
b = input("Please enter your username : ")
a_name = a.get("name")
a_pw = a.get("password")

if b == a["name"] :
    print(f"Hello, {a_name}! The password is : {a_pw}")
else:
    print(f"Hello, {a_name}! See you later.")
