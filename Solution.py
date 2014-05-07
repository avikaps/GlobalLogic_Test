import csv
from collections import OrderedDict, namedtuple

# Open a file as a read_file
with open('C:\\Users\\278967\\Desktop\\test3.csv') as r_file:
    reader = csv.reader(r_file)
    # Create an output tuple !! 
    out_tuple = namedtuple('Output', ['Highest_Price', 'Year', 'Month'])
    # Create an empty ordered dictionary
    Ordr_Dict = OrderedDict()
    # Get all the company names after index 2
    Company_Names = next(reader)[2:]
    # Add those names into ordered dictionary
    for Company in Company_Names:
        Ordr_Dict[Company] = out_tuple(0, 'Year', 'Month')
    # Read the csv row by row
    try:
        for row in reader:
            year, month = row[:2]
        for Company, price in zip(Company_Names, map(int, row[2:])):
            #Check if the price in the ordered dictionay is higher
            if Ordr_Dict[Company].Highest_Price < price:
                Ordr_Dict[Company] = out_tuple(price, year, month)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

# Iterate over ordered dictionary to get fancier output
for items in Ordr_Dict.iteritems():
    print items


# This has been tested over the sample CSV create by the file named "create_csv.py"  - Allthough the file
# created by the script is not perfect, we have manually replace (',"' and '",') with white spaces.

# The output produced as follows :
# ('Company-A', Output(Highest_Price=991, Year='1993', Month='Feb'))
# ('Company-B', Output(Highest_Price=993, Year='2000', Month='Sep'))
# ('Company-C', Output(Highest_Price=990, Year='2005', Month='Aug'))
# ('Company-D', Output(Highest_Price=1000, Year='1993', Month='Feb'))
# ('Company-E', Output(Highest_Price=994, Year='2001', Month='May'))
# ('Company-F', Output(Highest_Price=1000, Year='2008', Month='Feb'))
# ('Company-G', Output(Highest_Price=997, Year='1998', Month='Nov'))
# ('Company-H', Output(Highest_Price=999, Year='2011', Month='Dec'))
# ('Company-I', Output(Highest_Price=995, Year='2011', Month='Dec'))
# ('Company-J', Output(Highest_Price=1000, Year='1998', Month='Aug'))
