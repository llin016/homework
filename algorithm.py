csv = open("grades.csv","r")
def bestletterGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

with open('grades.csv','r') as grade_file:
    reader = csv.reader(grade_file)
student_grade = {}
for row in reader:
    student_name,score = row[0],float(row[1])
    if student_name in student_grade:
        student_grade[student_name] = max(student_grade[student_name],score)
    else:
        student_grade[student_name] = score
   

def calculateGrade(studentName):
    if studentName in student_grade:
       score = student_grade[student_name]
    return calculateGrade(score)
    else:
    return "No Grade"

csv.close()







