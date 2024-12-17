def my_func():
    print("Hello world")

my_func()

def my_str():
    hello = "Good Morning, Welcome back"
    print(hello)

my_str()

def my_var(name):
    print(name)

my_var("Bob")
my_var("Peter")
my_var("George")

def my_con(firstname):
    print("Hello "+ firstname + " Please enter!")
my_con("Abas")

def two(name,age):
    print("Hello " + name + "you are " + str(age) + " years old")
two("Bob ",23)

def welcome(firstname,lastname,age):
    print("Hello "+ firstname + " "+lastname+ " you are "+str(age) +" years old")
welcome("Moi","William",68)

def summation(num1,num2):
    print(num1+num2)
summation(18,29)

def promoted(name,age):
    if age > 5 and age<7:
        return f"{name} You are {age} years old, promoted to grade 1"
    elif age ==7:
        return f"{name} You are {age} years old, promoted to grade 2"
    promoted("Bob",7)