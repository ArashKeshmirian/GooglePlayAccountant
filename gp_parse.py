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
        if row[7] == "com.limbic.ac130":
            if row[14] in totals:
                totals[row[14]] = float(totals[row[14]])+float(row[15])
            else:
                totals[row[14]] = float(row[15])
            # if row[14] in totals:
            #     totals[]
            # if row[14]=="USD":
                # total += float(row[15])
        linenum += 1;
    # print header
    for currency in totals:
        print currency, totals[currency]
    # print totals