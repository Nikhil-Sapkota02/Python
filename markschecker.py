StudentMarks = []
for i in range(20):
    StudentMarks.append(int(input("Enter The Total Marks Of A Student: ")))

StudentNames = []
for i in range(20):
    StudentNames.append(input("Enter the name of the student: "))

for i in range(20):
    if StudentMarks[i] >= 30:
        print(StudentNames[i] + " is passed")
    else:
        print(StudentNames[i] + " is failed")