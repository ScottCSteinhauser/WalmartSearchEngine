import csv
import math
from sklearn.cluster import KMeans
import numpy as np

data_list = []

categories = set(["Fashion", "Electronics", "Home", "Baby", "Toys", "Food", "Pets", "Beauty", "Personal Care","Arts, Crafts & Sewing"])

fashion = ["Fashion", "Featured Brands", "Women", "Men", "Clothing", "Jewelry"]
electronics = ["Electronics", "TV & Video", "Computers", "Cell Phones", "Wearable Tech", "iPad & Tablets", "Home Audio & Theater", "Video Games", "Portable Audio", "Cameras & Camcorders", "Smart Home"]
home = ["Home", "Household Essentials"]
baby = ["Baby", "Baby Registry", "Car Seats", "Strollers", "Nursery", "Baby & Toddler Toys", "Diapering", "Feeding"]
toys = ["Toys", "Musical Instruments"]
food = ["Food"]
pets = ["Pets", "Pet Supplies"]
beauty = ["Beauty", "Premium Beauty"]
personal_care = ["Personal Care", "Oral Care", "Shave", "Bath & Body"]
arts_crafts_sewing = ["Arts, Crafts & Sewing"]

# load data into dictionary
products = {}
hold = [fashion, electronics, home, baby, toys, food, pets, beauty, personal_care, arts_crafts_sewing]
categorySet = []
for x in hold:
    categorySet += x
points = []
names = []
def categoryToValue(category):
    for i in range(len(categorySet)):
        if category in categorySet[i]:
            return float(i)/len(categorySet)

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False

with open('info4.csv', 'r+') as product_data:
    csv_reader = csv.reader(product_data, delimiter=",", quotechar='"')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            keywords = row
            line_count += 1
        else:
            name = row[0]
            print(row[2])
            if not check_float(row[2]):
                continue
            price = float(row[2])
            category = row[-1]
            normalizedPrice = math.log(float(price), 10)
            normalizedCategory = categoryToValue(category)
            if normalizedCategory is None:
                continue
            products[name] = [normalizedPrice, normalizedCategory, normalizedCategory]
            points += [products[name]]
            names += [name]

    # now run k means clustering on points
    print(points)
    npPoints = np.array(points)
    kmeans = KMeans(n_clusters=100, random_state=0).fit(npPoints)
    print(kmeans.labels_)
    for i in range(len(names)):
        if kmeans.labels_[i] == 54:
            print(names[i], 10**points[i][0])
    # now loop back through csv, getting cluster of each particular product and rewriting to new csv.
with open('info4.csv', 'r+') as product_data:
    csv_reader = csv.reader(product_data, delimiter=",", quotechar='"')
    with open('clustered_info.csv', mode="wb") as info_file:
        info_writer = csv.writer(info_file, delimiter=",", quotechar='"')
        line = 0
        print("dumb")
        for row in csv_reader:
            if line == 0:
                info_writer.writerow(row + ['cluster'])
                line += 1
                continue
            if not check_float(row[2]):
                continue
            category = row[-1]
            normalizedCategory = categoryToValue(category)
            if normalizedCategory is None:
                continue
            info_writer.writerow(row + [kmeans.labels_[line-1]])
            line += 1
            print(line)

print(categorySet)


"""
with open('clean_info.csv', mode = "w", encoding="utf8") as info_file:
    info_writer = csv.writer(info_file, delimiter = ",", newline = "")

    for row in data_list:
        info_writer.writerow(row)
"""
