import csv
from csv import DictWriter

headersCSV = ['Roll','Branch','Name','Class','Section','Exam','Maths','Chemistry','Physics','BME','BEE']

reader = csv.DictReader(open("data.csv"))

def Student():
    print("""\nWelcome To Student Management System

    Enter 1 : To View Student's List 
    Enter 2 : To Add New Student 
    Enter 3 : To Search Student 
    Enter 4 : To Remove Student 
		
	""")

    userInput = int(input("Please Select An Above Option: "))

    if(userInput == 1):
        data=[]
        with open("data.csv") as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                data.append(row)
        col=[x[0]for x in data]
        print("Roll\tName\tBranch\tClass\tSection\tExam\tMaths\tChemistry\tPhysics\tBME\tBEE")
        for x in range(1,len(data)):
            print(data[x][0]+"\t"+data[x][2]+"\t"+data[x][1]+"\t"+data[x][3]+"\t"+data[x][4]+"\t"+data[x][5]+"\t"+data[x][6]+"\t"+data[x][7]+"\t\t"+data[x][8]+"\t"+data[x][9]+"\t"+data[x][10])

    elif(userInput == 2):
        print("Add New Student\n")
        Roll = input("Enter Roll No: ")
        Name = input("Enter Name: ")
        Branch = input("Enter Branch: ")
        Class = input("Enter Class: ")
        Section = input("Enter Section: ")
        Exam = input("Enter Exam Name: ")
        Maths = input("Enter Maths Marks: ")
        Chemistry = input("Enter Chemistry Marks: ")
        Physics = input("Enter Physics Marks: ")
        BME = input("Enter BME Marks: ")
        BEE = input("Enter BEE Marks: ")

        dict={'Roll':Roll,'Branch':Branch,'Name':Name, 'Class':Class, 'Section':Section, 'Exam':Exam, 'Maths':Maths, 'Chemistry':Chemistry, 'Physics':Physics, 'BME':BME, 'BEE':BEE} 
        with open('data.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
            dictwriter_object.writerow(dict)
            f_object.close()

    elif(userInput == 3):
        data = [] 
        with open("data.csv") as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                data.append(row)
            roll=input("Enter Roll Number: ")
            col=[x[0] for x in data]
            if roll in col:
                for x in range(0,len(data)):
                    if roll == data[x][0]:
                        print("\nStudent Exists:")
                        print("Roll: "+ data[x][0])
                        print("Branch: "+ data[x][1])
                        print("Name: "+ data[x][2])
                        print("Class: "+ data[x][3])
                        print("Section: "+ data[x][4])
                        print("Exam: "+ data[x][5])
                        print("Maths: "+ data[x][6])
                        print("Chemistry: "+ data[x][7])
                        print("Physics: "+ data[x][8])
                        print("BME: "+ data[x][9])
                        print("BEE: "+ data[x][10])
            else:
                print("Student Doesn't Exist")

    elif(userInput == 4):
        lines = list()
        roll= input("Please Enter Roll Number: ")
        with open('data.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == roll:
                        lines.remove(row)

        with open('data.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

#Main Function
Student()

def runAgain():
	runAgn = input("\nDo you Want To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):
		Student()
		runAgain()
	else:
		quit()

runAgain()	