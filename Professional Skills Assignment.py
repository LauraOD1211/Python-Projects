def main():
    sales = []
    vatlist = []
    vat = 0
    total = 0
    print("SALES CALCULATOR")
    print("Enter sales figures, or -1 to quit")
    temp=float(input("Please enter the sales figures: "))
    while (temp!=-1):
        sales.append(temp)
        temp=float(input("Please enter the sales figures: "))

    print("The sales figures entered were",sales)

    for x in sales:
        total += x
        temp = x*.23
        dec2 = "%.2f" % (x+temp)
        vatlist.append(dec2)
        vat += temp
        total += temp

    total = "%.2f" % total
    vat = "%.2f" % vat

    print("The sales figures including VAT were", vatlist)
    print("The total VAT charged is", vat)
    print("The total sales for this period are", total)

main()
