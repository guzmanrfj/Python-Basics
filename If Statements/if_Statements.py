from csv import reader

# Abrir el archivo especificando codificación UTF-8
with open('AppleStore.csv', encoding='utf-8') as opened_file:
    read_file = reader(opened_file)
    apps_data = list(read_file)
opened_file.close()

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    price = float(row[5])

    if price == 0.0:
        free_apps_ratings.append(rating)

avg_rating_free = sum(free_apps_ratings)/len(free_apps_ratings)
print(sum(free_apps_ratings))
print(len(free_apps_ratings))
print(avg_rating_free)