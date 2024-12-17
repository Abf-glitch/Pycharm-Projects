num1 = int(input("How much are you withdrawing?"))
num2 =int(input("What is you pin?"))

if num1 > 20000:
    print("You have withdrawn above the recom!")
else:
    print("Transction Failed")
if num1 >10000:
    print("You have withdrawn the recom!")
else:
    print("Transction Successful")

if num1 < 10000:
    print("You have withdrawn below the recom!")
else:
    print("Transction Failed")