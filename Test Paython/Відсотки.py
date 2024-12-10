deposit = float(input("Введіть суму (в гривнях): "))
Percentages = float(input("Введіть відсоток: "))
a = Percentages / 12 / 100
x = round(deposit * a, 2)
print("Щомісячна виплата: " , x)