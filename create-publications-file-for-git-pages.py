#!/usr/bin/env python

import sys

for line in open("/Users/joevineis/Documents/MY-PAPERS/All-citations.csv",'r', errors='ignore'):
    x = line.strip().split(',')
    filename=x[4]+"_"+x[0].split(';')[0].split(".")[0]+"_"+x[2]+"_"+x[3]
    outfile =open(filename+".md", 'w')
    outfile.write("---"+'\n'+
                  "title: "+'"'+x[1]+'"'+'\n'+
                  "collection: publications"+'\n'+
                  "permalink: /publication/"+filename+'\n'+
                  "excerpt: "+"'"+x[1]+"'"+'\n'+
                  "date: "+x[4]+'\n'+
                  "venue: "+"'"+x[2]+"'"+'\n'+
                  "paperurl: "+"'"+"http://academicpages.github.io/files/"+x[4]+"_"+x[0].split(';')[0].split(".")[0]+"_"+x[3]+".pdf'"+'\n'+
                  "---"+'\n'+
                  "[Download paper here] (http://academicpages.github.io/files/"+x[4]+"_"+x[0].split(';')[0].split(".")[0]+"_"+x[3]+".pdf)")
