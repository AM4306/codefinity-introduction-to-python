produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries = [produce] + [dairy]

for g in range(len(groceries)):
    section = groceries
    for i in range(len(section)):
        item = section
        print(item)

print(f"Item name:{item}")