import csv
import random
Data = []
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for yr in range(1990, 2014):
    for Mnths in months :
        Data.append(yr)
        Data.append(Mnths)
        for num in range(0, 10):
            rand_num = random.randint(1,1000)
            Data.append(rand_num)
        Data.append('\n')
            
with open('C:\\Users\\278967\\Desktop\\test3.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    Header = [['Year', 'Month', 'Company-A','Company-B','Company-C','Company-D','Company-E','Company-F','Company-G','Company-H','Company-I','Company-J'],Data]
    a.writerows(Header)
    for rows in a :
        rows.replace(',"' , ' ') & rows.replace('",' , ' ')

    
        

