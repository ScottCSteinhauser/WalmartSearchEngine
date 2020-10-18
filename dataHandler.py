import csv
import re

data_list = []

categories = set()

with open('info.csv', encoding = "utf8") as product_data:
    csv_reader = csv.reader(product_data, delimiter = ",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            keywords = row
            line_count += 1
        else:
            row[0] = re.sub(r'[^\w\s]', '', row[0]).lower()
            row[5] = re.sub(r'[^\w\s]', '', row[5]).lower()
            row[6] = re.sub(r'[^\w\s]', '', row[6]).lower()
            categories.add(row[7])
            data_list.append(row)
            line_count += 1
        print(f"Line Count: {line_count}")

print(categories)

"""
with open('clean_info.csv', mode = "w", encoding="utf8") as info_file:
    info_writer = csv.writer(info_file, delimiter = ",")

    for row in data_list:
        info_writer.writerow(row)
"""