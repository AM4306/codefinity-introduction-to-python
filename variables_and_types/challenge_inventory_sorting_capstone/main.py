# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# items
candy1 = items[0:9]
print(candy1)

candy2 = items[11:20]
print(candy2)

dry_goods = items[22:]
print(dry_goods)

# Caategories
category1 = categories[0:11]
print(category1)

category2 = categories[13:24]
print(category2)

bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

print(f"We have {candy1} for {bubblegum_price} in the {category1}")
print(f"We have {candy2} for {chocolate_price} in the {category1}")
print(f"We have {dry_goods} for {pasta_price} in the {category2}")
