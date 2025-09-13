from student import Allstudents

class Allteachers:
    all_Teachers = []
    subject_list = {
        "Phy": [],
        "Chem": [],
        "Maths": [],
        "Comp": [],
        "English": []
    }
    
    def __init__(self, name, address, phone_number, teachingsubject, T_id):
        self.name = name 
        self.address = address 
        self.phone_number = phone_number
        self.teachingsubject = teachingsubject
        self.T_id = T_id
    
    def display_details(self):
        print(f"""
        Name: {self.name}
        Address: {self.address}
        Phone Number: {self.phone_number}
        Subject: {self.teachingsubject}
        Teacher ID number: {self.T_id}
        """)
        
    @classmethod
    def search_teacher(cls, teacherID):
        for teacher in cls.all_Teachers:
            if teacher.T_id == teacherID:
                print("Teacher Found")
                teacher.display_details()
                return teacher
            
        print("Teacher NOT FOUND")
        return None
            
class AddTeachers(Allteachers):
    def __init__(self, name, address, phone_number, teachingsubject, T_id):
        super().__init__(name, address, phone_number, teachingsubject, T_id)
        Allteachers.all_Teachers.append(self)
        print("TEACHER ADDED SUCCESSFULLY")
        
class DeleteTeacher:
    def __init__(self, TeacherID): 
        self.TeacherID = TeacherID
        Teacher_to_delete = None
        for teacher in Allteachers.all_Teachers:
            if teacher.T_id == self.TeacherID:
                Teacher_to_delete = teacher
                break
        
        if Teacher_to_delete:
            Allteachers.all_Teachers.remove(Teacher_to_delete)
            category = Teacher_to_delete.teachingsubject
            if category in Allteachers.subject_list:
                Allteachers.subject_list[category].remove(Teacher_to_delete)
                print(f"Teacher with Teacher ID {TeacherID} deleted Successfully")
            else:
                print("Teacher not found in subject list!!")
        else:
            print("Teacher not found!!")

class AssignSubject:
    def __init__(self, TeacherID, teachingsubject):
        self.teachingsubject = teachingsubject
        self.TeacherID = TeacherID
        assign = None
           
        for teacher in Allteachers.all_Teachers:
            if teacher.T_id == self.TeacherID:
                assign = teacher
                break
        
        if assign:
            category = self.teachingsubject
            if category in Allteachers.subject_list:
                Allteachers.subject_list[category].append(assign)
                print(f"Teacher {assign.name} assigned to {category}")
            else:
                print("Subject not found in subject list!")
        else:
            print("Teacher not found!")

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
            category = (self.grade,self.Subject.lower())
            for key in Allstudents.student_marks.keys():
                if key == category:
                    Allstudents.student_marks[key].append((ID.name,self.marks))
                    print("Marks Successfully added")
                    break
        else:
            print("Student not found")
            
if __name__ == "__main__":
    pass







