volume = int(input("Введите необходмый объём раствора (мл): "))
mass = volume * 0.009
water  = volume

with open("recipe.txt", "w", encoding="utf-8") as file:

    file.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n - * 23\n Общий объём: {volume} мл\n Масса сооли: {mass:.2f} г\n Объём воды: {water} мл\n")
repeat = "-" * 23
print(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n {repeat}\n Общий объём: {volume} мл\n Масса сооли: {mass:.2f} г\n Объём воды: {water} мл\n")
print("Рецепет сохранен в  файл")