time: int = int(input("Введите время падения (в секундах): ")) #ввод значении
result: int = (pow(time,2)*10)//2							   #вычисление глубины
print("Глубина колодца: ",result," метров")