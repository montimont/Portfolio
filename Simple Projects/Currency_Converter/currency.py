
print("""

1 - British Pound (GBP)
2 - Canadian Dollar (CAD)
3 - Chinese Yuan (CNY)
4 - Euro (EUR)
5 - United States Dollar (USD)

""")
      
start_currency = int(input("Select a starting currency (1-5):  "))
end_currency = int(input("Select a ending currency (1-5):  "))

if start_currency == 1:
    if end_currency == 2:
        amount = int(input("Enter your amount in GBP:  "))
        convert = round((amount * 1.670093),2)
        print(f'GBP: {amount} \nCAD: {convert}')
    elif end_currency == 3:
        amount = int(input("Enter your amount in GBP:  "))
        convert = round((amount * 8.479533),2)
        print(f'GBP: {amount} \nCNY: {convert}')
    elif end_currency == 4:
        amount = int(input("Enter your amount in GBP:  "))
        convert = round((amount * 1.135577),2)
        print(f'GBP: {amount} \nEUR: {convert}')
    elif end_currency == 5:
        amount = int(input("Enter your amount in GBP:  "))
        convert = round((amount *1.2345),2)
        print(f'GBP: {amount} \nUSD: {convert}')
    elif start_currency == end_currency:
        print("It is the same currency!")
    else:
        print("Not a valid currency")

elif start_currency == 2:
    if end_currency == 1:
        amount = int(input("Enter your amount in GBP:  "))
        convert = round((amount * 0.598857),2)
        print(f'CAD: {amount} \nGBP: {convert}')
    elif end_currency == 3:
        amount = int(input("Enter your amount in GBP:  "))
        convert = round((amount * 5.077281),2)
        print(f'CAD: {amount} \nCNY: {convert}')
    elif end_currency == 4:
        amount = int(input("Enter your amount in GBP:  "))
        convert = round((amount * 0.679948),2)
        print(f'CAD: {amount} \nEUR: {convert}')
    elif end_currency == 5:
        amount = int(input("Enter your amount in GBP:  "))
        convert = round((amount * 0.73918),2)
        print(f'CAD: {amount} \nUSD: {convert}')
    elif start_currency == end_currency:
        print("It is the same currency!")
    else:
        print("Not a valid currency")


elif start_currency == 3:
    if end_currency == 1:
        amount = int(input("Enter your amount in CNY:  "))
        convert = round((amount *0.117931),2)
        print(f'CNY: {amount} \nGBP: {convert}')
    elif end_currency == 2:
        amount = int(input("Enter your amount in CNY:  "))
        convert = round((amount *0.196956),2)
        print(f'CNY: {amount} \nCAD: {convert}')
    elif end_currency == 4:
        amount = int(input("Enter your amount in CNY:  "))
        convert = round((amount *0.13392),2)
        print(f'CNY: {amount} \nEUR: {convert}')
    elif end_currency == 5:
        amount = int(input("Enter your amount in CNY:  "))
        convert = round((amount * 0.145586),2)
        print(f'CNY: {amount} \nUSD: {convert}')
    elif start_currency == end_currency:
        print("It is the same currency!")
    else:
        print("Not a valid currency")

elif start_currency == 4:
    if end_currency == 1:
        amount = int(input("Enter your amount in EUR:  "))
        convert = round((amount *0.880609),2)
        print(f'EUR: {amount} \nGBP: {convert}')
    elif end_currency == 2:
        amount = int(input("Enter your amount in EUR:  "))
        convert = round((amount *1.4707),2)
        print(f'EUR: {amount} \nCAD: {convert}')
    elif end_currency == 3:
        amount = int(input("Enter your amount in EUR:  "))
        convert = round((amount *7.467157),2)
        print(f'EUR: {amount} \nCNY: {convert}')
    elif end_currency == 5:
        amount = int(input("Enter your amount in EUR:  "))
        convert = round((amount * 1.087112,2))
        print(f'EUR: {amount} \nUSD: {convert}')
    elif start_currency == end_currency:
        print("It is the same currency!")
    else:
        print("Not a valid currency")


elif start_currency == 5:
    if end_currency == 1:
        amount = int(input("Enter your amount in USD:  "))
        convert = round((amount * 0.810045),2)
        print(f'USD: {amount} \nGBP: {convert}')
    elif end_currency == 2:
        amount = int(input("Enter your amount in USD:  "))
        convert = round((amount * 1.35285),2)
        print(f'USD: {amount} \nCAD: {convert}')
    elif end_currency == 3:
        amount = int(input("Enter your amount in USD:  "))
        convert = round((amount * 6.8681291),2)
        print(f'USD: {amount} \nCNY: {convert}')
    elif end_currency == 4:
        amount = int(input("Enter your amount in USD:  "))
        convert = round((amount * 0.919868),2)
        print(f'USD: {amount} \nEUR: {convert}')
    elif start_currency == end_currency:
        print("It is the same currency!")
    else:
        print("Not a valid currency")
else:
    pass
