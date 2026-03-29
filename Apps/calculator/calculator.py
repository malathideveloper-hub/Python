
#App intro
print("*****Calulator App*****")
print("supports only Interger number - version: 1")

#get the input from user using command line args
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
choice = int(input("Enter which operation you need to perform (input the choice number): \n1.add \n2.sub \n3.mul \n4.div\n"))

#conditional check 
if choice == 1:
    print("You have chosen the Add ...")
    print("Answer is : ",num1+num2)
elif choice == 2:
    print("You have chosen the Sub ...")
    print("Answer is : ",num1-num2)
elif choice == 3:
    print("You have chosen the Mul ...")
    print("Answer is : ",num1*num2)
elif choice == 4:
    print("You have chosen the Div ...")
    print("Answer is : ",num1/num2)
else:
    print("You have chosen an invalid choice")
    
print("Thank you for using the simple calculator app - We will enhance it in next versions")