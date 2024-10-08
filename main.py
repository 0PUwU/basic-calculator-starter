# Owen Perez
# OCT 8 2024
# BASIC-Calculsator-starter

print("""Chose a math operation to perform:
      1. Addition (+)
      2. Subtraction (-)
      3. Multiplication (*)
      4. Division (/)
      """)

choice = int(input("Enter your choice (1-4): "))

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter second number: "))

answer1 = num1 + num2
answer2 = num1 - num2
answer3 = num1 * num2
answer4 = num1 % num2

if choice == 1:
    print(f"{num1} plus {num2} is {answer1}")
elif choice == 2:
    print(f"{num1} minus {num2} is {answer2}")
elif choice == 3:
    print(f"{num1} multipled by {num2} is {answer3}")
elif choice == 4:
    print(f"{num1} divided by {num2} is {answer4}")
else:
    print("Invaid number")