#!/usr/bin/python
import csv
import sys

if len(sys.argv) < 2:
    print "Usage: ./gp_parse.py <filename>"
    

sourcefile = sys.argv[1]

print "Reading from", sourcefile, "..."

""" read the source file """
with open(sourcefile, 'rb') as csvfile:
    gp_reader = csv.reader(csvfile)
    linenum = 0
    products = {}
    header = ""

    for row in gp_reader:
        if linenum == 0:
            header = row
        elif row[7] in products:
            if row[17] in products[row[7]]:
                product = products[row[7]]
                product[row[17]] = float(product[row[17]]) + float(row[18])
            else:
                product = products[row[7]]
                product[row[17]] = float(row[18])
        else:
            products[row[7]] = {row[17]:row[18]}
        linenum += 1;
    for product in products:
        for currency in products[product]:
            print product, currency, products[product][currency]
        
    # code used to print header-row information for CSV
    # index = 0
    # print "\n"
    # for column in header:
    #     print index, column
    #     index += 1
    