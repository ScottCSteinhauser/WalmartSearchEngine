import csv
import re

data_list = []

categories = set(["Fashion", "Electronics", "Home", "Baby", "Toys", "Food", "Pets", "Beauty", "Personal Care", "Arts, Crafts & Sewing"])

fashion = ["Fashion", "Featured Brands", "Women", "Men", "Clothing", "Jewelry"]
electronics = ["Electronics", "TV & Video", "Computers", "Cell Phones", "Wearable Tech", "iPad & Tablets", "Home Audio & Theater", "Video Games", "Portable Audio", "Cameras & Camcorders", "Smart Home"]
home = ["Home"]
baby = ["Baby", "Baby Registry", "Car Seats", "Strollers", "Nursery", "Baby & Toddler Toys", "Diapering", "Feeding"]
toys = ["Toys"]
food = ["Food"]
pets = ["Pets", "Pet Supplies"]
beauty = ["Beauty", "Premium Beauty"]
personal_care = ["Personal Care", "Oral Care", "Shave", "Bath & Body"]
arts_crafts_sewing = ["Arts, Crafts & Sewing"]

ugly_data_list = []

with open('nodupsall.csv', 'r+', encoding = "utf8") as product_data:
    csv_reader = csv.reader(product_data, delimiter = ",", quotechar = '"')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            keywords = row
            line_count += 1
        else:
            if line_count % 2 == 0:
                if row[7] == "Clothing":
                    line_count += 1
                    continue
                if row[7] == "Home" or row[7] == "Arts, Crafts & Sewing" or row[7] == "Arts Crafts & Sewing":
                    line_count += 1
                    continue
            if line_count % 3 == 0:
                if row[7] == "Home" or row[7] == "Arts, Crafts & Sewing" or row[7] == "Arts Crafts & Sewing":
                    line_count += 1
                    continue
            ugly_data_list.append(row.copy())
            row[0] = re.sub(r'[^\w\s]', '', row[0]).lower()
            row[5] = re.sub(r'[^\w\s]', '', row[5]).lower()
            row[6] = re.sub(r'[^\w\s]', '', row[6]).lower()
            categories.add(row[7])
            data_list.append(row)
            line_count += 1
        print(f"Line Count: {line_count}")


with open('trimmed_clean_nodupsall.csv', mode = "w", encoding="utf8", newline='') as info_file:
    info_writer = csv.writer(info_file, delimiter = ",")
    
    for row in data_list:
        info_writer.writerow(row)

with open('trimmed_ugly_nodupsall.csv', mode="w", encoding="utf8", newline='') as info_file:
    info_writer = csv.writer(info_file, delimiter=",")

    for row in ugly_data_list:
        info_writer.writerow(row)
