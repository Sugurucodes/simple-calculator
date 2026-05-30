print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = input("enter the choice: ")

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if choice == "1":
    print(num1 + num2)

if choice == "2":
    print(num1 - num2)

if choice =="3":
    print(num1 * num2)

if choice == "4":
    print(num1 / num2)
