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

# Example using the DictWriter class
fields = ['Name', 'Capital City', 'Largest City', 'Population']

state_info = [
    {
        "Name": "Colorado",
        "Largest City": "Denver",
        "Capital City": "Denver",
        "Population": "5773714"
    }, {
        "Name": "Connecticut",
        "Largest City": "Hartford",
        "Capital City": "Bridgeport",
        "Population": "3605944"
    }, {
        "Name": "Delaware",
        "Largest City": "Dover",
        "Capital City": "Wilmington",
        "Population": "989948"
    }
]

with open("statedata.csv", "a", newline="") as filecsv:
    writer = csv.DictWriter(filecsv, fields)
    writer.writerows(state_info)
