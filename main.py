meters = float(input("Введіть кількість метрів: "))

print("Оберіть одиницю вимірювання для конвертації:")
print("1. Милі")
print("2. Дюйми")
print("3. Ярди")
choice = int(input("Введіть номер одиниці вимірювання (1, 2 або 3): "))

if choice == 1:
    miles = meters * 0.000621371
    print(f"{meters} метрів дорівнює {miles} миль")
elif choice == 2:
    inches = meters * 39.3701
    print(f"{meters} метрів дорівнює {inches} дюймів")
elif choice == 3:
    yards = meters * 1.09361
    print(f"{meters} метрів дорівнює {yards} ярдів")
else:
    print("Некоректний вибір одиниці вимірювання")

