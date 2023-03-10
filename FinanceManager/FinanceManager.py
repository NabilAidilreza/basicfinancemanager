import os
import os.path
import csv
from datetime import datetime


def main():
    if os.path.isfile('Finances.csv'):
        # Do Something
        while True:
            print('##### Finance Manager #####')
            print('')
            print('1. Show All')
            print('2. Add One Record')
            print('3. Add Multiple Records')
            print('4. Calculate Total By Month')
            print('5. Open CSV File with Excel')
            print('6. Close Program')
            print('\n')
            option = str(input('Option Number? : '))
            print('')
            if option == '1':    
                with open('Finances.csv','r') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        print(row)
                    print('\n')
            elif option == '2':
                WriteToCSV()
            elif option == '3':
                times = str(input('Number of items to add: '))
                if times.isdigit() == True:
                    num = int(times)
                    while num != 0:
                        WriteToCSV()
                        num -= 1
                    print(times + ' records have been added. \n')
                else:
                    print('Not a number \n')
            elif option == '4':
                month = str(input('Which Month?: '))
                valid = False
                MONTHS = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
                if len(month) < 3:
                    print('Invalid Input (i.e Jan or January) \n')
                elif len(month) == 3 and month.upper() in MONTHS:
                    test_month = month.upper()
                    valid = True
                elif len(month) > 3 and month[:3].upper() in MONTHS:
                    test_month = month[:3].upper()
                    valid = True
                else:
                    print('Invalid Input (i.e Jan or January) \n')
                if valid == True:
                    index = MONTHS.index(test_month)
                    print(index)

                ## INCOMPLETE ##
            elif option == '5':
                openFile('Finances.csv')
            elif option == '6':
                break
            else:
                print('Invalid Option')
    else:
        # Create New Instance
        file = open('Finances.csv', 'a',newline = '')
        writer = csv.writer(file)
        HEADER = ['DATE','NAME','PRICE','STATUS']
        writer.writerow(HEADER)
        file.close()
        main()


def WriteToCSV():
    with open('Finances.csv','a',newline = '') as csvfile:
        writer = csv.writer(csvfile)
        now = datetime.now()
        DATE = now.strftime("%m/%d/%Y")
        NAME = str(input('Item Name?: '))
        PRICE = str(input('Item Price?: '))
        INPUT = [DATE,NAME,PRICE,'Valid']
        writer.writerow(INPUT)
        print('')
        print('Record Added \n')
        
def openFile(filename):
    os.startfile(filename)


if __name__ == "__main__":  #runs the function main() automatically
    main()  
