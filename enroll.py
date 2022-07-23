computerScience=[]
networking=[]
desktopSupport=[]
softwareProgramming=[]
computerSales=[]
acceptedStudents=[computerScience,computerSales,networking,desktopSupport,softwareProgramming]


print("###############################################################")
print("WELCOME TO IT SYSTEMS ACADEMY")
print("###############################################################")
#Personal Details
firstName=input("Enter your first name")
lastName=input("Enter your last name")
age=int(input("Enter your age"))
idNumber=input("Enter your id number")
emailAddress=input("Enter your email")
phoneNumber=input("Enter your phone number")
homeAddress=input("Enter your home address")

#Programmes you interested in
print("##############################################################")
print("We offer the following programmes:","\n Computer Science \n Networking \n Desktop Support \n Software Programming \n Computer Sales")

#Qualifications
#Prompt the user to enter his grade high school grades
mathsScore=input("Enter your Mathematics score")
fullName= firstName + lastName
welcomeMessage="Hello"+fullName+",you have been accepted to study"

if mathsScore =="A" :
    computerScience.append(fullName)
    print(welcomeMessage," Computer Science at IT Systems")
elif mathsScore =="B":
    softwareProgramming.append(fullName)
    print(welcomeMessage," Software Programming at IT Systems")
elif mathsScore =="C":
    networking.append(fullName)
    print(welcomeMessage," Networking at IT Systems")
elif mathsScore =="D":
    desktopSupport.append(fullName)
    print(welcomeMessage," Desktop Support at IT Systems")
elif mathsScore=="E":
    computerSales.append(fullName)
    print(welcomeMessage," Computer Sales at IT Systems")
else:
    print("Unfortunately",fullName," your application wasn't successfully better luck next time")
