pricelist = [1000, 2000, 3000, 4000, 7000, 10000]
cash = int(input("Enter put price : "))
price = float(input("Enter share rate : "))
price1=price
if cash==3000:
    for i in range(4):
        price = price-price*2/100
        exit = price + price*2/100
        print(round(price, 2), pricelist[i+2], "cp+2")
if cash==1000:
    for i in range(5):
        price = price-price*2/100
        exit = price + price*2/100
        print(round(price, 2), pricelist[i+1], "cp+2")
print(price1+round(price1*2/100, 2))
