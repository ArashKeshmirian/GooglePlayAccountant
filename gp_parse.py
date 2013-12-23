#!/usr/bin/python
import csv
import sys
import os


def main():
    if len(sys.argv) < 2:
        print("Usage: ./gp_parse.py <filename>")
        return
    
    kProductIndex = 7
    kMerchantCurrencyNameIndex = 17
    kMerchantCurrencyValueIndex = 18

    sourcefile = sys.argv[1]

    """ read the source file """
    with open(sourcefile, 'rb') as csvfile:
        gp_reader = csv.reader(csvfile)
        linenum = 0
        products = {}
        header = ""

        for row in gp_reader:
            if linenum == 0:
                header = row
            elif row[kProductIndex] in products:
                if row[kMerchantCurrencyNameIndex] in products[row[kProductIndex]]:
                    product = products[row[kProductIndex]]
                    product[row[kMerchantCurrencyNameIndex]] = (float(product[row[kMerchantCurrencyNameIndex]]) + 
                                                                float(row[kMerchantCurrencyValueIndex]))
                else:
                    product = products[row[kProductIndex]]
                    product[row[kMerchantCurrencyNameIndex]] = float(row[kMerchantCurrencyValueIndex])
            else:
                products[row[kProductIndex]] = {row[kMerchantCurrencyNameIndex]:row[kMerchantCurrencyValueIndex]}
            linenum += 1;
        
        # output
        print("\nFor file: %s"%(os.path.basename(sourcefile)))
        for product in products:
            for currency in products[product]:
                print("\tProduct: %s\n\t\t%s %s"%(product, currency, products[product][currency]))
        
        # code used to print header-row information for CSV
        # index = 0
        # print "\n"
        # for column in header:
        #     print index, column
        #     index += 1

if __name__ == "__main__":
  main()