# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing is about to begin:")

for i in inventory:
    data = inventory[i]
    current_stock = data[0]
    min_stock     = data[1]
    restock_quant = data[2]
    on_sale       = data[3]
    print(f"processing", inventory)
    while current_stock < min_stock:
        current_stock += restock_quant
        inventory[i][0] = current_stock
    if current_stock > discount_threshold and not on_sale:
        inventory[i][3] = True

print("Processing completed")
    
    
    
