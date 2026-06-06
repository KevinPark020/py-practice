class Student:

    __slots__ = ["__id", "__name", "__credits", "__gpa", "__courses"]

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__credits = 0
        self.__gpa = 0.0
        self.__courses = []

    def add_course(self, course):

        self.__courses.append(course)
        self.__credits += course.get_credits()


    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_credits(self):
        return self.__credits
    
    def get_gpa(self):
        return self.__gpa
    
    def set_credits(self, credits):
        return self.__credits + credits
    
    def set_gpa(self, gpa):
        return self.__gpa + gpa
    
class Course:

    __slots__ = ["__name", "__credits", "__grade"]

    def __init__(self, name, credits, grade):

        self.__name = name
        self.__credits = credits
        self.__grade = grade

    def get_name(self):
        return self.__name
    
    def get_credits(self):
        return self.__credits
    
    def get_grade(self):
        return self.__grade

        
    
def print_student(student):

    print("Student:", student.get_id(), student.get_name(), student.get_credits(), student.get_gpa())

def print_course(course):
    print("Course:", course.get_name(), course.get_credits(), course.get_grade())




def main():
    # student1 = Student()
    # student2 = Student()
    
    # student1.id = "1234"
    # student1.name = "Callie"
    # student1.credits = 89
    # student1.gpa = 3.7
    
    # student2.id = "5678"
    # student2.name = "Taehun"
    # student2.credits = 39
    # student2.gpa = 3.5
    
    # print_student(student1)
    # print_student(student2)
    callie = Student("1234", "Callie")
    tae = Student("4567", "Taehun")
    print_student(callie)
    print_student(tae)

    gccis1 = Course("GCCIS-123", 4, "A")
    gccis2 = Course("GCCIS-124", 4, "A")
    dmath = Course("Discrete Mathematics", 3, "B-")
    cal2 = Course("Calculus 1", 3, "A-")

    print_course(gccis1)
    print_course(gccis2)
    

    
if __name__ == "__main__":
    main()
    
    
    
