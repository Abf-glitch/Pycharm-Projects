class Student:
    def __init__(self, firstname, course, gender):
        self.Firstname = firstname
        self.Course = course
        self.Gender = gender

    def study(self):
        print(self.Firstname, "is studying")


student1 = Student("John", "Cybersecurity", "Male")
student1.study()

student2 = Student("Neema", "Data Science", "Female")
student2.study()

student3 = Student("Makena", "MIT", "Female")
student3.study()
