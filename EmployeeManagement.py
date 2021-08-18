#Employee Management System - Collects Employee Basic Details
#Author: Arul
#Created Date: 16/08/2021
#Modified Date: 18/08/2021

import re
from datetime import datetime

def ValidateId(count):
    print("Your ID is ACE000{}".format(count))
   
def ValidateSpace(Name):
        yes = bool(re.search(r"\s",Name))
        if(yes == True):
            print("INVALID NAME. Name should not contain space.")
            ValidateName()
        elif(yes == False):
            ValidateNumerics(Name)
           
def ValidateNumerics(Name):
    yes = any(chr.isdigit() for chr in Name)
    if(yes == True):
            print("INVALID NAME. Name should not contain numbers.")
            ValidateName()
    elif(yes == False):
            ValidateSpecialCharacters(Name)
           
def ValidateSpecialCharacters(Name):
    yes = re.compile('[@_!#$%^&*()<>?/\|}{~:+=-]')
    if(yes.search(Name) == None):
        ValidateRepetition(Name)
    else:
        print("INVALID NAME. Name should not contain special characters.")
        ValidateName()
       
def ValidateRepetition(Name):
    i=0
    for length in range(1,(len(Name)-1)):
        if((Name[length-1]==Name[length]) and (Name[length]==Name[length+1])):
            print("INVALID NAME. Renter a valid name")
            break
        i+=1
    if((i+2)==len(Name)):
        print("Hello {}".format(Name))
       
       
def ValidateName():
    Name = input("Enter your name : ")
    if(len(Name)<3):
        print("INVALID NAME. Enter a valid name with 3 or more characters.")
        ValidateName()
    elif(len(Name)>=3):
        ValidateSpace(Name)

def ValidateBirth():
    Date = str(input('Enter your DOB in dd/mm/yyyy format : '))
    try:
        Date = datetime.strptime(Date, '%d/%m/%Y')
    except ValueError:
        print("Incorrect format")
        ValidateBirth()
    PresentYear = datetime.now().year
    if Date.month > datetime.now().month:age =  PresentYear - Date.year -1
    elif Date.month <= datetime.now().month:age =  PresentYear - Date.year
   
    if((int(age)>18) and int(age)<61):
        print("Your age is {}".format(age))
        ValidateDOJ(age)
    if int(age)<=17:
        print("Enter Valid DOB. You are too young")
        ValidateBirth()
    if int(age)>60:
        print("Enter Valid DOB. You must have completed your service")
        ValidateBirth()
       
def ValidateDOJ(age):
    JoiningDate = str(input("Enter your Date of Joining in dd/mm/yyyy format : "))
    try:
        JoiningDate = datetime.strptime(JoiningDate,'%d/%m/%Y')
    except ValueError:
        print("Incorrect format")
        ValidateDOJ(age)
    experience = int(datetime.now().year - JoiningDate.year)
    if age-experience < 18:
        print("INVALID DOJ")
        ValidateDOJ(age)
    if age-experience >= 18:
        print("You are {} years experienced".format(experience))

def ValidateEmail():
    Email = input("Enter your email ID : ")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex,Email)):
        print("Valid Email {}".format(Email))
    else:
        print("INVALID EMAIL")
        ValidateEmail()

def ValidateMobile():
    MobileNum = input("Enter your Mobile Number. Number should contain 10 digits and should not start between 0-5: ")
    Pattern = r"^[189][0-9]{9}$"
    if(re.search(Pattern, MobileNum)):
        print("VALID Number {}".format(MobileNum))
    else:
        print("INVALID NUMBER. Please a valid number.")
        ValidateMobile()

def ValidateSalary():
    amount = int(input("Enter your salary : "))
    if amount == 0:
        print("INVALID SALARY. Enter correct salary")
        ValidateSalary()
    elif amount > 0:
        print("Your Salary is {}".format(amount))

def ValidateQualification():
    print("Qualifications : 1)B.E ECE 2)B.E EEE 3)B.E CSE  4)B.TECH IT ")
    choose = input("Pick your qualification- 1 or 2 or 3 or 4 : ")
    if choose == '1':print("Qualification : B.E ECE")
    elif choose == '2':print("Qualification : B.E EEE")
    elif choose == '3':print("Qualification : B.E CSE")
    elif choose == '4':print("Qualification : B.TECH IT")
    elif choose >= '5':
        print("INVALID QUALIFICATION")
        ValidateQualification()
     
count = 1
while count!=0:
    ValidateId(count)
    ValidateName()
    ValidateBirth()
    ValidateEmail()
    ValidateMobile()
    ValidateSalary()
    ValidateQualification()
    choice = input("Do you want to continue(Y/N) ? ")
    choice = choice.upper()
    if choice == "Y":
        count+=1
    elif choice == "N":
        count = 0