# taking input from the user
num1 = int(input("Enter your first number:\n"))
num2 = int(input("Enter your second number:\n"))

# deciding the action
action = int(input("What action do you want?\n1. For plus (1)\n2. For minus (2)\n3. For multiply(3)\n4. For divide(4)\nEnter your answer:"))

# performing the action and printing the result
if action < 1 or action > 4:
    print("please enter a valid argument")

elif action == 1:
    ans = str(num1 + num2)
    print("the answer is: " + ans)

elif action == 2:
    ans = str(num1 - num2)
    print("the answer is: " + ans)

elif action == 3:
    ans = str(num1 * num2)
    print("the answer is: " + ans)

elif action == 4:
    ans = str(num1 / num2)
    print("the answer is: " + ans)
