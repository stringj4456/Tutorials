import csv

# Example use of csv.reader function
print("CSV Reader Function Example:")
with open("username.csv", newline="") as File:
    reader = csv.reader(File, delimiter=";")
    for row in reader:
        print(row)

print()

# Example using the DictReader class
print("DictReader Class Example:")
with open("username.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        print(row)

# Example writing using the csv.writer function
state_info = ["California", "Sacramento", "Los Angeles", "39538223"]
with open("state_data.csv", "a", newline="") as state_file:
    writer = csv.writer(state_file)
    writer.writerow(state_info)

