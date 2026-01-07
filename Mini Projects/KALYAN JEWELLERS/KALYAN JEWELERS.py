print("KALYAN JEWELLERS".center(50, "-"))  
name = input("\nEnter your name: ")
gender = input("Enter gender (M|F): ").upper()
age = int(input("Enter age: "))

grand_total = 0
grand_discount = 0
grand_making = 0
item_no = 0

gold_price_per_gram = 5752
making_charge_per_gram = 845

while True:
    item_no += 1
    product = input("\nEnter product: ")
    grams = float(input("Enter product grams: "))
    print(f"Current gold price per gram: Rs {gold_price_per_gram}")

    print("-" * 40)

    total_gold_price = grams * gold_price_per_gram
    print(f"TOTAL GOLD RATE: Rs {total_gold_price}")

    # Making charges calculate 
    total_making_charge = grams * making_charge_per_gram
    print(f"Total Making Charges: Rs {total_making_charge}")

    print("-" * 40)

    # Total amount before discount
    total_amount = total_gold_price + total_making_charge
    print(f"TOTAL AMOUNT: Rs {total_amount}")

    # Discount calculation
    discount = 0
    
    if gender == 'M':
        if age > 65:
            if 200000 < total_gold_price <= 300000:
                discount = 20
            elif 300000 < total_gold_price <= 500000:
                discount = 30
            elif total_gold_price > 500000:
                discount = 35
        else:
            if 200000 < total_gold_price <= 300000:
                discount = 10
            elif 300000 < total_gold_price <= 500000:
                discount = 20
            elif total_gold_price > 500000:
                discount = 25
                
    elif gender == 'F':
        if age > 65:
            if 200000 < total_gold_price <= 300000:
                discount = 25
            elif 300000 < total_gold_price <= 500000:
                discount = 35
            elif total_gold_price > 500000:
                discount = 40
        else:
            if 200000 < total_gold_price <= 300000:
                discount = 15
            elif 300000 < total_gold_price <= 500000:
                discount = 25
            elif total_gold_price > 500000:
                discount = 30       

    print(f"DISCOUNT: {discount}%")

    # Discount amount
    discount_amount = (discount / 100) * total_gold_price
    print(f"DISCOUNT AMOUNT: Rs {discount_amount}")

    print("-" * 40)

    # Net amount
    net_amount = total_amount - discount_amount
    print(f"TOTAL NET AMOUNT (for {product}): Rs {net_amount}")

    # Add to totals
    grand_total += net_amount
    grand_discount += discount_amount
    grand_making += total_making_charge

    print("-" * 40)

    choice = input("Press Y to continue or N to exit: ").lower()
    if choice == 'n':
        print("\n" + "-" * 50)
        print("FINAL BILL")
        print("-" * 50)
        print(f"Your name: {name}")
        print(f"Your gender: {gender}")
        print(f"Your age: {age}")
        
        print(f"Total items purchased: {item_no}")
        print(f"Name of the product: {product}")
        print(f"TOTAL MAKING CHARGES: Rs {grand_making}")
        print(f"TOTAL DISCOUNT GIVEN: Rs {grand_discount}")
        print(f"GRAND TOTAL BILL: Rs {grand_total}")
        print("Thank you for shopping at Kalyan Jewellers!")
        print("-" * 50)
        break
