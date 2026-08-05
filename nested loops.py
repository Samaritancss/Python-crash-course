#nested loop = A loop within another loop(outer, inner)
#                 outer loop:
#                    inner loop:

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter the symbol: ")

for x in range(rows):
    for y in range(columns):
     print(symbol, end="")
    print()

