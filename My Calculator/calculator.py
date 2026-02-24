
def calculate_profit():

    cost_tl=  float(input("input cost per can(TL):"))


    box= 12

    cost_box_tl = cost_tl * box

    print("Full box costs: ", cost_box_tl)

    cargo_usd = float(input("cargo fee(USD): "))

    local_cargo_cedis = float(input("transport from Accra to Techiman or Kumasi to Techiman (GHS): "))

    number_of_box = int(input("How many boxes: "))

    if number_of_box <= 0:
       print("Number of boxes must be greater than zero")
       return()



    
    tl_ghs_rate = float(input("TL to GHS rate: "))
    usd_ghs_rate = float(input("USD to GHS rate: "))
    profit_margin = float(input("Desired profit margin (%): "))


    # convert product cost

    cost_box_gh = cost_box_tl * tl_ghs_rate

    # convert cargo to ghs

    cargo_usd_ghs = cargo_usd * usd_ghs_rate


    #Total cargo per box

    cargo_per_box = (local_cargo_cedis + cargo_usd_ghs) / number_of_box

    #total cost per box
    total_cost_per_box = cost_box_gh + cargo_per_box


    # Selling price
    selling_price = total_cost_per_box * (1+profit_margin/100)

    break_even_price = total_cost_per_box


    print("\n--- shipment summary---")
    print("break even price: ", round(break_even_price, 2))
    print("selling price: ", round(selling_price, 2))

    
   
while True:
    calculate_profit()
    again = input("\nRun another simulation? (yes/no): ").lower()
    if again != "yes":
        print("Existing the system. Calculation mode off.")
        break


    


