grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}
# retrieve
print(grocery_inventory.get("Bread"))
bread_details = (117, "Bakery")
# add new item:
grocery_inventory.update({"Cookies": (143, "Bakery")})
# remove item:
grocery_inventory.pop("Eggs")
# output:
print("Details of Bread:", bread_details)
print("Inventory after adding Cookies:", grocery_inventory)
print("Inventory after removing Eggs:", grocery_inventory)