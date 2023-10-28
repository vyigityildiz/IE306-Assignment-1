import random

# Stochastically creates a demand size
def create_demand():
    p = random.random()
    if p <= 0.1:
        return 2
    elif p <= 0.28:
        return 3
    elif p <= 0.48:
        return 4
    elif p <= 0.7:
        return 5
    elif p <= 0.9:
        return 6
    else:
        return 7

# Returns order size, order shipment day
def create_order(inv, wanted):
    return (wanted - inv), random.randint(0, 5)

# Main simulation method
def simulate(days, init_inv):
    inv = init_inv
    lost = 0
    order_date = None
    cumul_inv = 0
    for day in range(days):
        demand = create_demand()

        # Demand handling
        if demand <= inv:
            inv -= demand
        else:
            inv = 0
            lost += demand - inv
        
        # Ordering and order handling
        if inv <= 10 and order_date is None:
            order_size, order_date = create_order(inv, 20)
            order_date = day + order_date
        if day == order_date:
            inv += order_size
            order_date = None
        cumul_inv += inv
    return lost / days, cumul_inv / days

print(simulate(10, 18))
        