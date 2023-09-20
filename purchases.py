import sys

def add_tax(num_list,tax):
    tax_list = []
    for i, value in enumerate(num_list):
        tax_list.append(value + value*tax)
    return tax_list

#Inputs
try:        
    purchases = int(input("Number of purchases: "))
except:
    print("Number of purchases must be a whole number!")
    sys.exit()
try:
    tax = float(input("Salex tax: "))
except:
    print("Tax must be a number!")
    sys.exit()

#Creating the list 
customers = []
costs = []
for i in range(0,purchases):
    customers.append(input("Customer: "))
    costs.append(float(input("Cost: ")))
costs = add_tax(costs, tax)

result = {}
for i, value in enumerate(customers):
    if value in result:
        result[value] = result[value] + costs[i]
    else:
        result[value] = costs[i]
#Output
print(result)
