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
    totals = {}
    header = ""

    for row in gp_reader:
        if linenum == 0:
            header = row
        elif row[7] == "com.limbic.ac130":
            # parse report, put into totals dict by currency
            if row[17] in totals:
                totals[row[17]] = float(totals[row[17]])+float(row[18])
            else:
                totals[row[17]] = float(row[18])
        else:
            print "Unknown Product",row[7]
            # todo(AK): store each new product in a dict
        linenum += 1;
    for currency in totals:
        print currency, totals[currency]
        
    # code used to print header-row information for CSV
    # index = 0
    # print "\n"
    # for column in header:
    #     print index, column
    #     index += 1
    