products_and_prices = input().split(",")

tobuy_list = []
total_value = 0
max_product = {
    "brand":"None",
    "price": 0
}

for e in products_and_prices:
    brand,price = e.split(":")
    price = int(price)
    tobuy_list.append(
        {
            "brand":brand,
            "price": price
        }
    )
    total_value += price

    if price > max_product["price"]:
        max_product["brand"] = brand
        max_product["price"] = price

for e in tobuy_list:
    print("{} : {}".format(e["brand"],e["price"]))
print("Sum : {}".format(total_value))
print("Top : {}".format(max_product["brand"]))
    