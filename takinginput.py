Marks = []
for i in range(8):
    Marks.append(int(input("Enter the Marks of Eight Subjects: ")))
    if Marks[i] >= 30:
        print("You are a pass")

    else:
        print("You are a fail")