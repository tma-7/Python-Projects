#Calculator 
#Goal: Make a calculator that conducts the 4 basic operations (add, subtract, multiply, and divide) for two numbers
# 8/11/2025 | 6:00 PM EST

num_1 = float(input("What is your first number? :"))
num_2 = float(input("What is your second number? : "))
op = input("What is your operation? | Add -> + | Subtract -> - | Multiply -> * | Divide -> / | : ")

if op == "+":
    a = round((num_1 + num_2), 2)
    print(f'The answer is {a}')

elif op == '-':
    b = round((num_1 - num_2), 2)
    print(f"The answer is {b}")

elif op == "*":
    c = round((num_1 * num_2), 2)
    print(f"The answer is {c}")

elif op == '/':
    d = round((num_1 / num_2), 2)
    print(f"The answer is {d}")

else:
    print(f"{op} is an invalid operator") 

