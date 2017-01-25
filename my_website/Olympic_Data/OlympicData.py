import matplotlib.pyplot as plt
import os.path

def stripNumber(dirtyNumber):
    retval=""
    usedDecimal = False
    for c in dirtyNumber:
        if c in '0123456789':
            retval += c
        elif c =='.' and not usedDecimal:
            retval += c
            usedDecimal = True
    if retval =='':
        retval = "0"
    return retval

def results_to_sec(result):
    parts = result.split(':')
    if isNumber(parts[0]):
        retval = int(parts[0])*60
        retval += float(stripNumber(parts[1]))
    else:
        retval = 0
    return retval

def lstr(string, length):
    retval=""
    if len(string)<length:
        retval = string
    else:
        for i in range(length):
            retval += string[i]
    return retval

def isNumber(string):
    retval = True
    try:
        x=float(string)
    except ValueError:
        retval = False
    return retval

#Name the current directory
directory = os.path.dirname(os.path.abspath(__file__))

#Make lists to hold year and Number of people
yearsMen = []
yearsWomen = []
resultsMen = []
resultsWomen = []

# For each year form 1880 to 2012...
# Open teh data file for specified year
filename = os.path.join(directory, 'mens1500.csv')
fileMens = open(filename,'r') # r means read only
filename = os.path.join(directory, 'womens1500.csv')
fileWomens = open(filename, 'r')

#Skip Header line in both files
next(fileMens)
next(fileWomens)

# For each line in the file
for line in fileMens:
    # Split the line into the three separate pieces of info
    lineList = line.split(',')
    year = lineList[0]
    medal = lineList[3]
    result = lineList[5]
    result = (results_to_sec(result))
    # If the name matches...
    #if lstr(event, 5) == '1500m' and int(year) >= 1972:
    if isNumber(result) and medal.upper()=="GOLD" and int(year) >= 1972:
        yearsMen.append(year)
        resultsMen.append(result)

for line in fileWomens:
    # Split the line into the three separate pieces of info
    lineList = line.split(',')
    year = lineList[0]
    medal = lineList[3]
    result = lineList[5]
    result = (results_to_sec(result))
    # If the name matches...
    #if lstr(event, 5) == '1500m' and int(year) >= 1972:
    if isNumber(result) and medal.upper()=="GOLD" and int(year) >= 1972:
        yearsWomen.append(year)
        resultsWomen.append(result)

print 'Mens: ' + str(len(yearsMen))
print 'Womens: ' + str(len(yearsWomen))
fileMens.close()
fileWomens.close()

fig, ax = plt.subplots(1,1)
ax.plot(yearsMen, resultsMen,'#0000FF')
ax.plot(yearsWomen, resultsWomen,'#FF0000')

strTitle = 'Mens 1500m times (blue), '
strTitle += 'Womens 1500m times (red)'
ax.set_title(strTitle)
fig.show()
