from __future__ import print_function
import fitz
import sys, time, re


def processcontent (inputfile,outputfile):
    doc = fitz.open(inputfile)

    npages = len(doc)

    f = open(outputfile,"w+")

    alltext = ""

    for i in range(0, npages):
        page = doc.loadPage(i)
        text = page.getText(output = "text")
        alltext.join(text)
        #print("page: %s, text: %s" %(i, text) )
        f.write("%s" %text)

    f.close();

    return alltext





