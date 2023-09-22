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
if purchases < 0:
    print(f"Did you mean {purchases * -1}?")
    sys.exit()
elif purchases == 0:
    print("Why are you even here if you haven't bought anything?")
    sys.exit()
try:
    tax = float(input("Sales tax: "))
except:
    print("Tax must be a number!")
    sys.exit()
if tax < 0:
        print("We're in a Capitalist society, but I'll calculate it anyways :)")
#Creating the list 
customers = []
costs = []
for i in range(0,purchases):
    customers.append(input("Customer: "))
    try:
        costs.append(float(input("Cost: ")))
    except:
        print("Must input a number!")
        sys.exit()
costs = add_tax(costs, tax)

result = {}
for i, value in enumerate(customers):
    if value in result:
        result[value] = result[value] + costs[i]
    else:
        result[value] = costs[i]
#Output
print(result)
