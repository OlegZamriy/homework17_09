num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

print("Оберіть операцію:")
print("1. Сума трьох чисел")
print("2. Добуток трьох чисел")
choice = int(input("Введіть номер операції (1 або 2): "))

if choice == 1:
    result = num1 + num2 + num3
    print("Сума трьох чисел:", result)
elif choice == 2:
    result = num1 * num2 * num3
    print("Добуток трьох чисел:", result)
else:
    print("Некоректний вибір операції")

