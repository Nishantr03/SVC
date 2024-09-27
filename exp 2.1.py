a=int(input("Enter the number of students you want to enter :"))
record={}
for i in range (a):
    name=input("Enter the name of student :")
    b=int(input("how many subjects marks you want to enter :"))
    marks = list()
    for i in range(0,b):
        marks.append(int(input("Enter the marks :")))
        record[name]=marks
print("The record is :",record)

x=input("Enter the student you want to find average of:")
y=(record.get(x))
avg=sum(y)/len(y)
print("The average marks:","%.2f"%avg)




