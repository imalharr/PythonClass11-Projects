n=int(input("Enter number of students: "))
students={}
for i in range(n):
    r=int(input("Roll: "))
    name=input("Name: ")
    marks=int(input("Marks: "))
    students[r]=(name,marks)
for r in students:
    if students[r][1]>75:
        print(students[r][0])