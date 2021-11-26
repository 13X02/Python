row = int(input("Enter the number of rows"))
col = int(input("Enter the number of columns"))
symbol = input("Enter the symbol")

for i in range(row):
    for j in range(col):
        print(symbol, end="")
    print()