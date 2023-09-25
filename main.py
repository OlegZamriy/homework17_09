num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

print("Оберіть операцію:")
print("1. Максимум")
print("2. Мінімум")
print("3. Середньоарифметичне")
choice = int(input("Введіть номер операції (1, 2 або 3): "))

if choice == 1:
    result = max(num1, num2, num3)
    print("Максимум із трьох чисел:", result)
elif choice == 2:
    result = min(num1, num2, num3)
    print("Мінімум із трьох чисел:", result)
elif choice == 3:
    result = (num1 + num2 + num3) / 3
    print("Середньоарифметичне трьох чисел:", result)
else:
    print("Некоректний вибір операції")

