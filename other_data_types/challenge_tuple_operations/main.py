# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
# Count
print(shelf.count("apples"))
apple_count = 3
print(f"Number of Apples:", apple_count)
# find the index of bananas
print(shelf.index("bananas"))
banana_index = 2
print(f"First Banana Index:", banana_index)
# check


# Count
grapes_count = 1


# check
print(shelf.index("oranges"))
orange_index = 1


# output: 
print("Number of Apples:", apple_count)
print("First Banana Index:", banana_index)
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
    
if grapes_count <= 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

    
if "oranges" in shelf:
    print("Oranges are at index:", orange_index)


