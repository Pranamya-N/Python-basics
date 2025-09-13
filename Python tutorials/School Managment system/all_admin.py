class Password_student:
    password_storer = []
    def __init__(self):
        pass
    
    
    
def display_result(cls,studentID,studentgrade,subject):
    student_found = None 
    found = False
    for student in cls.all_students:
        if student.S_id == studentID:
            student_found = student
            break
    if student_found :
        key = (studentgrade ,subject)
        if key in cls.student_marks:
            print(f"\nMarks for {student.name} is:\n")
            for marks in cls.student_marks[key] :
                if marks[0] == student_found.name:
                    print(f"{subject.capitalize()} : {marks [1]}")
                    found = True
            if not found:
                print("\nMarks not added !!!")
        else:
            print("STUDENT NOT FOUND !!!")
    else:
        print("STUDENT NOT FOUND !!!")
        
        
class AddMarks:
    def __init__ (self,Subject,studentID,grade,Marks):
        self.studentID = studentID
        self.marks = Marks
        self.Subject = Subject
        self.grade = grade
        ID = None
        
        for student in Allstudents.all_students:
            if self.studentID == student.S_id:
                ID = student
                break
        if ID :
            key = (self.grade,self.Subject.lower())
            
            All_students.student_marks[key].append((student.name,self.marks))
            print("Marks Successfully added")
        else:
            print("Student not found")