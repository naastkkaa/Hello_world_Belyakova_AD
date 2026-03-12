dna = input("Введите последовательность ДНК: ").upper()
count_A = dna.count("A")
count_G = dna.count("G")
count_T = dna.count("T")
count_C = dna.count("C")

quantity = len(dna)

percentages_A = count_A / quantity * 100
percentages_G = count_G / quantity * 100
percentages_T = count_T / quantity * 100
percentages_C = count_C / quantity * 100

rt = "=" * 3
print(f"{rt} Анализ последовательности ДНК {rt} \n В верхнем регистре: {dna}\n")
print(f"Подсчет нуклеотидов: \n А: {count_A}\nG: {count_G}\nT: {count_T}\nC: {count_C}\n")
print(f"Общее количество нуклеотидов: {quantity}\n")
print(f"Процентное содержание нуклеотидов:\n A: {percentages_A}\n G: {percentages_G}\n T: {percentages_T}\n C: {percentages_C}\n")