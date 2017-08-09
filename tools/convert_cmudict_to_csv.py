#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 23:49:02 2017

@author: Rustem
"""
import re
import csv

def make_csv(fileName):
    outFile = open('metadata_from_cmudict.csv', "wb")
    writer = csv.writer(outFile, delimiter='|', quoting=csv.QUOTE_NONE) #
    with open(fileName) as f:
        for line in f:
            lineLessBreakets = line[line.find('(')+1:line.find(')')].strip()
            name = lineLessBreakets.split(" ")[0]
            text = ' '.join(lineLessBreakets.split(" ")[1:])
            textLessQuotes = text[1:-1]
            print textLessQuotes
            writer.writerow([name,textLessQuotes,textLessQuotes.replace('+', "")])
    outFile.close()       
    
    
if  __name__ ==  "__main__" :    
    make_csv('txt.done.data')            