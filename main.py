import csv
#################RETRIEVING-DATA######################
name = []
education = []
joinedYear = []
age = []
gender = []

with open("Employee.csv") as f:
  reader = csv.reader(f)
  for rows in reader:
    name.append(rows[0])

with open("Employee.csv") as f:
  reader = csv.reader(f)
  for rows in reader:
    education.append(rows[1])

with open("Employee.csv") as f:
  reader = csv.reader(f)
  for rows in reader:
    joinedYear.append(rows[2])

with open("Employee.csv") as f:
  reader = csv.reader(f)
  for rows in reader:
    age.append(rows[5])

with open("Employee.csv") as f:
  reader = csv.reader(f)
  for rows in reader:
    gender.append(rows[6])

print()

name.pop(0)
education.pop(0)
joinedYear.pop(0)
age.pop(0)
gender.pop(0)

age = [int(value) for value in age]
joinedYear = [int(value) for value in joinedYear]

dict = []

for i in range(len(name)):
  n = name[i]
  a = age[i]
  e = education[i]
  j = joinedYear[i]
  g = gender[i]
  dict.append({"Name": n,
                  "Age": a, 
                   "Education": e, 
                   "Joined Year": j, 
                   "Gender": g})

##################Make-Functions#############################

#Intro
def Intro(): 
  print()

  userInput = input("Hello, Welcome to Employee Managment Software, here are a few options of what you can do:\n\n" + "(A) Print all Dataset\n(P) Search Employee Data\n(S) Sort Employees and Employee Data\n(ADD) Add an Employee\n(R) Remove an Employee\n(M) Modify Employee Data\n\n" + "Enter your option: ")

  userInput = userInput.lower()

  if userInput == 's':
    Sort()
  elif userInput == 'a':
    AllData()
  elif userInput == 'm':
    Mod() 
  elif userInput == 'add':
    Add()
  elif userInput == 'd':
    d()
  elif userInput == 'r':
    Sub()
  elif userInput == 'p':
    EmployeeData()
  elif userInput != 'p' and 'a' and 's':
    print("\nThats not a option, lets try again")
    Intro()



#Print Data of Employee
def EmployeeData():
  print()
  name = input("Enter Employee Name: ")
  print()
  for dictionary in dict:
    if name in dictionary.values():
        print("---", dictionary["Name"], "---", "\nAge:", dictionary["Age"], "\nEducation:", dictionary["Education"], "\nJoined Year:", dictionary["Joined Year"], "\nGender:", dictionary["Gender"],  )
        break

#Print ALL Data
def AllData():
  print()
  print("Name", "\t", "Age", "\t", "Education", "\t", "Joined Year", "\t", "Gender")
  print()
  for x in dict:
    print(x["Name"], "\t",  x["Age"], "\t",  x["Education"], "\t",  x["Joined Year"], "\t\t\t",  x["Gender"], )

#Sorts Data
def Sort():
  inp = input("\nHeres some sorting options:\n\nAlphabetical Order from A to Z (AZ)\nAge from least to greatest (A)\nYear they joined staritng with those who came to recent (J)\n\nHow would you like to sort:")

  inp = inp.lower()
  
  if inp == 'az':
    def myFuc(i):
      return i["Name"]
    newDict = dict
    newDict.sort(key=myFuc)
    print("Name", "\t", "Age", "\t", "Education", "\t", "Joined Year", "\t", "Gender")
    print()
    for x in newDict:
      print(x["Name"], "\t",  x["Age"], "\t",  x["Education"], "\t",  x["Joined Year"], "\t\t\t",  x["Gender"], )
  elif inp == 'a':
    def myFuc(i):
      return i["Age"]
    newDict = dict
    newDict.sort(key=myFuc)
    print("Name", "\t", "Age", "\t", "Education", "\t", "Joined Year", "\t", "Gender")
    print()
    for x in newDict:
      print(x["Name"], "\t",  x["Age"], "\t",  x["Education"], "\t",  x["Joined Year"], "\t\t\t",  x["Gender"], )
  elif inp == 'j':
    def myFuc(i):
      return i["Joined Year"]
    newDict = dict
    newDict.sort(key=myFuc)
    print("Name", "\t", "Age", "\t", "Education", "\t", "Joined Year", "\t", "Gender")
    print()
    for x in newDict:
      print(x["Name"], "\t",  x["Age"], "\t",  x["Education"], "\t",  x["Joined Year"], "\t\t\t",  x["Gender"],)

#Add
def Add():
  n = input("\nLets add a new Employee! Enter Name: ")
  a = input("\nNow enter their Age: ")
  e = input("\nNow enter their Education: ")
  j = input("\nNow the present Year: ")
  g = input("\nNow enter their Gender: ")
  dict.append({
    "Name": n,
    "Age": a, 
    "Education": e, 
    "Joined Year": j, 
    "Gender": g})
  print()
  print("All set! Welcome " + n + "!")

#Sub
def Sub():
  print()
  name = input("Who will we eliminate today, eneter their name: ")
  for dictionary in dict:
    if name in dictionary.values():
      dict.remove(dictionary)

#Mod
def Mod():
  name = input("Who's data do you want to change? Enter name: ")
  print()
  change = input("What exactly would you like to change? Enter option: ")
  print()
  new = input("What will you put in for this information? Enter new data: ")
  for dictionary in dict:
    if name in dictionary.values():
      dictionary[change] = new
      print(dictionary)
      


###################Main###################

Intro()

while True: 
  userInput = input("\nWant to do something else [y/n]: ")

  if userInput == "y": 
    Intro()
  else: 
    exit()
    
