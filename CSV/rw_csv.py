import csv

# Example use of csv.reader function
print("CSV Reader Function Example:")
with open("username.csv", newline="") as File:
    reader = csv.reader(File, delimiter=";")
    for row in reader:
        print(row)

print()
print("DictReader Class Example:")
# Example using the DictReader class
with open("username.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        print(row["Username"],row["Identifier"])

