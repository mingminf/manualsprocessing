import countwordfrequency
import extracttext


extracttext.processcontent("./manuals/srp3013_27_dfu_aen.pdf", "./manuals/srp3013_27_dfu_aen.txt")

## Open the file with read only permit
f = open('./manuals/srp3013_27_dfu_aen.txt', "r")

## use readlines to read all lines in the file
## The variable "lines" is a list containing all lines

data=f.read().replace('\n', '')

fullwordlist = countwordfrequency.stripNonAlphaNum(data)
wordlist = countwordfrequency.removeStopwords(fullwordlist, countwordfrequency.stopwords)
dictionary = countwordfrequency.wordListToFreqDict(wordlist)
sorteddict = countwordfrequency.sortFreqDict(dictionary)

for s in sorteddict:
    print(str(s))

## close the file after reading the lines.
f.close()