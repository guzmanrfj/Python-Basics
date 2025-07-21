###
# opened_file = open('AppleStore.csv')
#from csv import reader
#read_file = reader(opened_file)
#apps_data = list(read_file)
#opened_file.close()

#free_apps_ratings = []
#for row in apps_data[1:]:
#    rating = float(row[7])
    
    # Complete the code from here

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

all_ratings = []
for row in apps_data[1:]:
    rating = float(row[8])
    all_ratings.append(rating)
    
avg_rating = sum(all_ratings)/len(all_ratings)
print(avg_rating)
print(len((all_ratings)))
print(sum(all_ratings))    