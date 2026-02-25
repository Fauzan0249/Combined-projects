

def calculate_profit():
    print("\n====== Shipment Calculation ======")

    cost_tl = float(input("Input cost per can (TL): "))
    box = 12
    cost_box_tl = cost_tl * box

    cargo_usd = float(input("Cargo fee (USD): "))
    local_cargo_cedis = float(input("Local transport (GHS): "))
    number_of_box = int(input("How many boxes: "))

    tl_ghs_rate = float(input("TL to GHS rate: "))
    usd_ghs_rate = float(input("USD to GHS rate: "))
    profit_margin = float(input("Desired profit margin (%): "))

    # Convert product cost to GHS
    cost_box_ghs = cost_box_tl * tl_ghs_rate

    # Convert cargo to GHS
    cargo_usd_ghs = cargo_usd * usd_ghs_rate

    # Cargo per box
    cargo_per_box = (local_cargo_cedis + cargo_usd_ghs) / number_of_box

    # Total cost per box
    total_cost_per_box = cost_box_ghs + cargo_per_box

    # Selling price
    selling_price = total_cost_per_box * (1 + profit_margin / 100)

    # Totals
    total_cost_all_boxes = total_cost_per_box * number_of_box
    revenue = selling_price * number_of_box
    profit_per_box = selling_price - total_cost_per_box
    total_profit = profit_per_box * number_of_box
    fixed_costs = local_cargo_cedis + cargo_usd_ghs
    
    
    if profit_per_box > 0:
        break_even_boxes = fixed_costs / profit_per_box
    else:
        break_even_boxes = 0

    return {
          "cost_per_box": total_cost_per_box,
           "selling_price":  selling_price,
           "profit_per_box": profit_per_box,
           "total_cost": total_cost_all_boxes,
           "revenue": revenue,
           "total_profit": total_profit,
           "break_even_boxes": break_even_boxes
    }


     

while True:
    results = calculate_profit()
     #Output
    print("\n===SHIPMENT SUMMARY======")
    print(f"cost per box (GHS): {results['cost_per_box']:.2f}")
    print(f"selling price per box (GHS): {results['selling_price']:.2f}")
    print(f"profitper box (GHS) : {results['profit_per_box']:.2f}")
    print("----------------------------------------")
    print(f"Total cost: {results['total_cost']:.2f}")
    print(f"Total revenue (GHS): {results['revenue']:.2f}")
    print(f"Total profit (GHS): {results['total_profit']:.2f}")
    print(f"Break_even_boxes: {results['break_even_boxes']:.2f}")
    print("=====================================")

    again = input("\nRun another simulation? (yes/no): ").lower()
    if again != "yes":
        print("Exiting system. Trade session closed.")
        break