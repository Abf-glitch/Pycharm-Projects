class Student:
    first_name = "Jacob"
    last_name = "Pedro"
    age = 19
    gender = "Male"

class Person:
    def __init__(self, name, residence, age, gender,marital_status):
        self.name = name
        self.residence = residence
        self.age = age
        self.gender = gender
        self.marital_status = marital_status
class Animal:
    def __init__(self, Carnivora,Herbivore):
        self.Carnivora = Carnivora
        self.Herbivore = Herbivore

class Employee():
    def __init__(self, name, salary, age, gender):
        self.name = name
        self.salary = salary
        self.age = age
        self.gender = gender
class Manager(Employee):
    def __init__(self, name, salary, age, gender,education_level):
        super().__init__(name,salary,age,gender)
        self.education_level = education_level
class Developer(Manager):
    def __init__(self, name, salary, age, gender,programming_language):
        super().__init__(name,salary,age,gender)
        self.programming_language = programming_language