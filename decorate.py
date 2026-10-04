# EXAMPLE 1 OF DECORATE
''' 
def morning():
    print("Sawez")

def decorate(func):
    def wrapper():
        print("MY name is  ")
        func()
        print("I am student !")
    return wrapper 

x = decorate(morning)
x()   
'''        

# EXAMPLE 2 of DECORATE
'''
def s():
    print("---UPGRADE COMPUTER CLASS---")

def x():
    print("")

def decorate(func):
    def wrapper():
        print("-------welcome to the------- ")
        func()
        print("----------PYTHON------------")
    return wrapper
a = decorate(s)
a()
'''

# EXAMPLE 3 OF DECORATE WITH [@]anternos


'''
def decorate(func):
    def wrapper():
        print("----FYBsc computer science----")
        func()
        print("------------THANKS------------")
    return wrapper

@decorate
def city_collge():
    print("welcome to the city college")
'''
'''
# EXAMPLE 4 OF DECORATE WITH ARGUMENTS

def decO(admission):
    def wrapper(*arg,**kwargs,):
        print("CITY COLLEGE")
        print(f"this is {len(arg)}")
        print(f"this is {len(kwargs)}")
        admission(*arg,**kwargs)
        print("THANKS YOU 🎉 !")
    return wrapper 

# @decO
# def first_year_addmission(sname,marks,round):
#     print(f"the student name ={sname}")
#     print(f"total marks ={marks}")
#     print(f"this is ={round}third round ")

# first_year_addmission("sawez",400,round=3)    

@decO
def info_student(sname,roll_number,age,marks,):
    print(f"STUDENT NAME IS = {sname}")
    print(f"STUDENT ROLL NUMBER = {roll_number}")
    print(f"STUDENT AGE = {age}")
    print(f"STUDENT TOTAL MARKS = {marks}")

  
info_student("sawez",roll_number=22,age=18,marks=150)
'''




def decorate(func):
    def wrapper():
        print("CHECK THE NUMBER IS ODD OR EVEN")
        func()
    return wrapper

@decorate
def check():
    number = int(input("Enter your number: "))

    if number % 2 == 0:
        print("NUMBER IS EVEN")
    else:
        print("NUMBER IS ODD")

check()




def first():
    print("password is invalid try again !")

def second():
    print("password valid ")    

def password():
    password = int(input("enter your password :"))
    if password == 5885:
        second()
    else:
        first()

password()    



               
