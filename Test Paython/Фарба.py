# Довжина - a , ширина - b , висота - h , площа - s , площа вікон у %- z , кількість фарби - x , ціна - y , s1 - площа без вікон .
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))
z = float(input("Введіть z: "))
s = round((a + b) * 2 * h, 2)
s1 = round(s * (1 - z / 100), 2)
x = round(s1 * 0.3, 2)
y = round(x * 300, 2)
print("Загальна площа: " , s)
print("Наявна площа: " , s1)
print("Кількість фарби: " , x)
print("Ціна фарби: " , y)