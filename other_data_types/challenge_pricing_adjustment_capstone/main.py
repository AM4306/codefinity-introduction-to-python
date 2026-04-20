# create a dictionary:
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 4.50, 30),
    "Bread": ("Bakery",2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}
# Check and update:
print(grocery_inventory.get("Eggs"))
price_of_eggs = grocery_inventory["Eggs"][1]
if price_of_eggs > 4:
    print("Eggs are too expensive, reducing the price by $1.")

else:
    print("The price of Egg is reasonable")
# Add a new item:
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
# Manage stock:
milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    print("milk needs to be restocked. increasing stock by 20 units.")
    grocery_inventory["Milk"] = (
    grocery_inventory["Milk"][0],      # category stays the same
    grocery_inventory["Milk"][1],      # price stays the same
    milk_stock + 20                    # add 20 to the old stock
)

else:
    print("Milk has sufficient stock.")
# remove item based on price:
price_of_apples = grocery_inventory["Apples"][1]
if price_of_apples > 2:
    (grocery_inventory.pop("Apples"))
    print("Apples removed from inventory due to high price.")
# final print 
print("Updated inventory:", grocery_inventory)
