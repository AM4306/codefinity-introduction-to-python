meat = ["Ham","3.99","50","Sliced"]
cheese = ["Cheddar","5.49","100","Sharp"]
condiment = ["Mustard","1.99","75","Spicy"]
meat_quantity = 50

# Main list:
deli_dept = [meat, cheese, condiment]
print("Initial Deli List:", deli_dept)

# restock item:
if ("Ham") in meat and meat_quantity < 100:
    meat[2] = 100
# add seasonal meat:
seasonal_meat = ["Turkey","4.50","100","Sliced"]
deli_dept.append(seasonal_meat)
# remove condiment:
deli_dept.remove(condiment)
# sort list:
deli_dept.sort()

# Output:
print(f"Updated Deli List:", deli_dept)

    
