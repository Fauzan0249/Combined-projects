#----- FAUZAN'S FINANCE APP-----

# Setting initial wallet balance

available_cash = 1000

while True:
      print("n\--- FINANCE MENU---")
      print(f"current cash: ${available_cash}")
      print("1. Calculate a receipt")
      print("2.Check if I can afford items")
      print("3.Exit App")


      choice = input("What would you like to do")

      if choice == "1":
            # Your receipt Logic
        item_price = float(input("item price:"))
        item_quantity = int(input("Quantity"))

        subtotal = item_price + item_quantity
        tax = float(input("Input tax rate")) * subtotal
        total = subtotal +  tax 

        print("Total cost: ${total}")


        #Ask if they want to pay

        pay = input("Will you pay for this now:")

        if pay == "Yes":
            available_cash -= total
            print("Paid! Wallet updated.")

      elif choice == "2":
      # Your budget logic
        item_one = float(input("Price of item 1:"))
        item_two = float(input("Price of item 2"))
        total_items = item_one + item_two


        if total_items <= available_cash:
            print("You have enough! Reamining: ${available_cash - total_items}")

        else:
            print("Not enough funds!")
      

      elif choice == "3":
          print("CLosing app. Goodbye!")
          break # Lopps stops


      else:
          print("Invalid option")