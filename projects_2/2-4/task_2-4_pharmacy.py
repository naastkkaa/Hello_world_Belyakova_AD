capsules = int(input("Введите общее количество прозведенных капсул: "))
capacity = int(input("Введите количество капсул в одной упаковке: "))

whole = capsules // capacity
remains = capsules % capacity

print(f"--- Отчет фасовочного цеха ---\n Полных упаковок: {whole}\n Остаток капсул: {remains}")
