#CALCULATING DISCOUNT-----
   
def discount_Regular(items_price):       #calculating discount for the regular customers
    discount = (items_price*10) / 100
    if items_price > 100:
        price_after_discount = items_price - discount 
    return price_after_discount

def discount_Premium(items_price):          #calculaing discount for the premium customers
    discount = (items_price*15) / 100
    if items_price > 100:
        price_after_discount = items_price - discount
    return price_after_discount


#CALCULATING AMOUNT FOR EACH ITEM-----
def main():
   
    a = [
            {"name": "Laptop", "price": 80.00, "quantity": 1, "category": "Electronics"},
            {"name": "Apple", "price": 1.50, "quantity": 4, "category": "Groceries"},
            {"name": "Broken Pen", "price": -5.00, "quantity": 1, "category": "Stationery"}, # Invalid price
            {"name": "Shirt", "price": 20.00, "quantity": 2, "category": "Clothing"},
            {"name": "Banana", "price": 0.50, "quantity": 2, "category": "Groceries"}
        ]

    cart_price = 0  #calculating total price of the cart.

    item_name = []   #declaring names of the items int list.
    item_category = set()  #declaring categries of items into set.

    for i in a:
        if i["price"] <= 0:
            continue
        elif i["price"] > 0:
            calculate = i["price"] * i["quantity"]
            cart_price += calculate
            item_name.append(i["name"])
            item_category.add(i["category"])

    
#CHECKING DISCOUNT FOR THE CUSTOMER-----
    if cart_price < 100:
            return cart_price
    else:
        customer_status = input("""Enter Customer status: 
        R for Regular
        P for Premium: """)

        if customer_status == "R":
            cart_price = discount_Regular(cart_price)
        elif customer_status == "P":
            cart_price = discount_Premium(cart_price)

    append_data = (item_name,item_category,cart_price)  #Storing all the data in tuple.
    
    print("append_data=",append_data)  #printing the tuple.

main()

    




