nutrient_medium = input("Название питательной среды:")
concentration = input("Концентрация агара (%):")
temperature = input("Температура стерилизации:")
medium = nutrient_medium.upper()
with open("recipe.txt", "w", encoding="utf-8") as recipe:
  recipe.write(f"{medium}\n {concentration}\n {temperature}\n")
print(f"Название питательной среды: {medium}\n Концентрация агара (%): {concentration}\n Температура стерилизации: {temperature}")
print("Файл 'recipe.txt' успешно сформирован!")