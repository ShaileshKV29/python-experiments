def show_grade(m1, m2, m3, m4, m5):
    marks = m1 + m2 + m3 + m4 + m5
    
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    elif marks >= 40:
        grade = "E"
    else:
        grade = "F"

    return grade

for i in range(5):
    sub1 = int(input("Enter Marks in Subject 1 : "))
    sub2 = int(input("Enter Marks in Subject 2 : "))
    sub3 = int(input("Enter Marks in Subject 3 : "))
    sub4 = int(input("Enter Marks in Subject 4 : "))
    sub5 = int(input("Enter Marks in Subject 5 : "))

    print("Grade is :", show_grade(sub1, sub2, sub3, sub4, sub5))