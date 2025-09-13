import pickle

class Allstudents:
    all_students = []
    student_lists = {
        ("Sci", 11, "Comp"): [],
        ("Sci", 11, "Bio"): [],
        ("Com", 11, "Comp"): [],
        ("Com", 11, "Acc"): [],
        ("Sci", 12, "Comp"): [],
        ("Sci", 12, "Bio"): [],
        ("Com", 12, "Comp"): [],
        ("Com", 12, "Acc"): [],
    }
    student_marks = {
            (11,"comp"):[],
            (11,"maths"):[],
            (11,"phy"):[],
            (11,"chem"):[],
            (11,"eng"):[],
            (11,"acc"):[],
            (11,"bio"):[],
            (12,"comp"):[],
            (12,"maths"):[],
            (12,"phy"):[],
            (12,"chem"):[],
            (12,"eng"):[],
            (12,"acc"):[],
            (12,"bio"):[]
        }
    def __init__(self, name, address,S_id, grade, faculty, major, Parents, Phone_number):
        self.name = name
        self.address = address
        self.S_id = S_id
        self.faculty = faculty
        self.father, self.mother = Parents
        self.fatherPhone_number, self.motherPhone_number = Phone_number
        self.grade = grade
        self.major = major
        

    def display_details(self):
        
        print(f"""
            Name = {self.name},
            Address = {self.address},
            Student ID number = {self.S_id},
            Faculty = {self.faculty},
            Grade = {self.grade},
            Parents = Father: {self.father}  Mother: {self.mother},
            PhoneNumber = FatherNum: {self.fatherPhone_number}  MotherNum: {self.motherPhone_number},
            Major Subject = {self.major}""")

    @classmethod    
    def search_student(cls, name):
        for student in cls.all_students:
            if student.name == name:
                print("\nStudent Found")
                student.display_details()
                return student
        print("Student Not Found !!!")
        return None
    
    @classmethod
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
                            
class Add_Student(Allstudents):
    def __init__(self, name, address, S_id, grade, faculty, major, Parents, Phone_number):
        super().__init__(name, address, S_id, grade, faculty, major, Parents, Phone_number)
        Allstudents.all_students.append(self)
        
        with open ("Students_Details.pkl","wb") as f:
            pickle.dump(Allstudents.all_students,f)
        
        print("\nStudent Added Successfully !!!\n")
        category = (self.faculty, self.grade, self.major)
        if category in Allstudents.student_lists:
            Allstudents.student_lists[category].append(self)

class DeleteStudent(Allstudents):
    def __init__(self, S_id):
        self.S_id = S_id
        student_to_delete = None
        for student in Allstudents.all_students:
            if student.S_id == self.S_id:
                student_to_delete = student
                break
        
        if student_to_delete:
            Allstudents.all_students.remove(student_to_delete)
            category = (student_to_delete.faculty, student_to_delete.grade, student_to_delete.major)
            if category in Allstudents.student_lists:
                Allstudents.student_lists[category].remove(student_to_delete)
            print(f"\nStudent with Student ID number: {self.S_id} deleted successfully!\n")
        else:
            print("Student Not Found for Deletion !!!")
        
class Displayfaculty:
    def __init__(self, faculty, grade, major):
        self.faculty = faculty
        self.grade = grade
        self.major = major

    def display_faculty_students(self):
        category = (self.faculty, self.grade, self.major)
        if category in Allstudents.student_lists:
            print(f'{self.grade} {self.faculty} ({self.major})\n')
            for student in Allstudents.student_lists[category]:
                student.display_details()
        else:
            print("No students found for this category.")

if __name__ == "__main__":
    pass
