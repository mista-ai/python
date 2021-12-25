products = []
print("Product analytics\n")
while True:
    print('''-----------------------
1 - add product(s)
2 - delete last product
3 - show analytics
4 - show products
5 - exit
-----------------------''')
    cin = input("Enter command: ")
    if cin.isdigit():
        cin = int(cin)
        if cin == 1:
            # add product(s)
            print("How many products do you want to enter?")
            while True:
                amount = input()
                if amount.isdigit():
                    amount = int(amount)
                    if amount == 0:
                        print("Wrong input. Enter a natural number.")
                    else:
                        for i in range(amount):
                            product = {}
                            product["name"] = input("Enter name of product: ")
                            while True:
                                price = input("Enter price of product: ")
                                if price.count('.') <= 1 and price.replace('.', '').isdigit():
                                    if price.count('.') == 0:
                                        price = int(price)
                                    else:
                                        price = float(price)
                                    product["price"] = price
                                    break
                                else:
                                    print("Wrong input. Enter a number.")
                            while True:
                                number = input("Enter number of product: ")
                                if number.isdigit():
                                    product["number"] = int(number)
                                    break
                                else:
                                    print("Wrong input. Enter a non-negative number.")
                            product["unit"] = input("Enter a unit: ")
                            products.append((len(products) + 1, product))
                        break
                else:
                    print("Wrong input. Enter a natural number.")
        elif cin == 2:
            # delete last product
            if len(products) > 0:
                products = products[:-1]
            else:
                print("There are no products")
        elif cin == 3:
            # show analytics
            if len(products) == 0:
                print("There are no products.")
            else:
                analytics = {"name": [], "price": [], "number": [], "unit": []}
                for prod in products:
                    for key in analytics.keys():
                        if prod[1][key] not in analytics[key]:
                            analytics[key].append(prod[1][key])
                for key in analytics.keys():
                    print(f'"{key}": {analytics[key]},')
        elif cin == 4:
            # show products
            if len(products > 0):
                for prod in products:
                    print(prod[0], prod[1])
            else:
                print("There are no products.")
        elif cin == 5:
            # exit
            break
        else:
            # wrong input
            print("wrong input. Try again")
    else:
        print("Wrong input. Try again.")