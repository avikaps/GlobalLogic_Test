import csv
from collections import OrderedDict, namedtuple

def process_csv(filename):
    check_filename(filename)
    # Open a file as a read_file
    with open(filename) as r_file:
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
        for row in reader:
            year, month = row[:2]
            for Company, price in zip(Company_Names, map(int, row[2:])):
                #Check if the price in the ordered dictionay is higher
                if Ordr_Dict[Company].Highest_Price < price:
                    Ordr_Dict[Company] = out_tuple(price, year, month)
    display_output(Ordr_Dict)

def display_output(Ordr_Dict):
    # Iterate over ordered dictionary to get fancier output
    for items in Ordr_Dict.iteritems():
        print items

def check_filename(filename):
    """ Return's TRUE if the file name is correct. """
    if filename.endswith('.csv'):
        print "\n Check passed -- file has a correct extension \n"
        return True
    else:
        print " \n Incorect format - Please use a file with '.csv' extension "
        return False
        
