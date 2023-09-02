radius: int = int(input("Введите радиус окружности: ")) 	#ввод значении
len_circle: int = 2 * radius * 3.14							#вычисление длины
square_circle: int = (pow(radius,2)*3.14)					#вычисление площади
print("Длина окружности:", len_circle,
      "Площадь круга", square_circle)