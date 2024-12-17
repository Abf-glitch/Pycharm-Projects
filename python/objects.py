from setuptools.command.develop import develop

from classes import Student, Manager, Developer
from classes import Person
from classes import  Animal
from classes import Employee
from classes import Manager
from classes import Developer
student1 = Student()
print(student1.first_name)
print(student1.last_name)
print(student1.age)
print(student1.gender)

person1 = Person('Alex', 'Nairobi', '56', "Male", "Married")
print(person1.name)
print(person1.age)
print(person1.gender)
print(person1.residence)
print(person1.marital_status)

animal1 =  Animal('lion','Elephant')
print(animal1.Carnivora)
print(animal1.Herbivore)

employee1 = Employee('Judy', 100000,36,'Male')
print(employee1.name)
print(employee1.salary)
print(employee1.age)
print(employee1.gender)
print(f'Name:{employee1.name},'
      f'Salary:{employee1.salary},'
      f'Age:{employee1.age},'
      f'Gender:{employee1.gender},')


manager1 = Manager('Paul',250000,35,'Male','Degree')
print(f'Name:{manager1.name},'
      f'Salary:{manager1.salary},'
      f'Age:{manager1.age},'
      f'Gender:{manager1.gender},'
      f'education_level:{manager1.education_level},')


developer1 = Developer('Paul',250000,35,'Male','Python')
print(f'Name:{developer1.name},'
      f'Salary:{developer1.salary},'
      f'Age:{developer1.age},'
      f'Gender:{developer1.gender},'
      f'programming language:{developer1.programming_language}')

