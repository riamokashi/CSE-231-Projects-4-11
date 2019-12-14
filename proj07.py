##################################################
# Computer proj 07
#
# file iteration with lists and tuples
# travel data for country by year  
# read 2 files 
# extract data from both files 
# sort data from both files in respective functions 
# return sorted data that will be inputed into other functions 
# display data for each request using string formatting 
# prepare to plot a bar graph and a line graph 
# plot the bar and line graph 
# create a loop to ask the user what they want to input and do with the functions 
####################################################

import matplotlib.pyplot as plt
import csv
from operator import itemgetter

MIN_YEAR = 2009
MAX_YEAR = 2017

def open_file(prompt_str):
    '''
        use try except to open a file 
    '''
    while True:
        #Iterating until correct path is fount
        filename = input(prompt_str)
        try:
            #Escaping if wrong path
            fp = open(filename, "r", encoding = "utf-8")
            break
        except FileNotFoundError:
            print('File not found! Try Again!')
            continue
    return fp

def read_travel_file(fp):
    '''
        read the travel file and return the sorted the data
    '''
    reader = csv.reader(fp)
    next(reader,None)
    res = [[], [], [], [], [], [], [], [], []]
    for line in reader:
        year = int(line[0])
        country_name = line[1][:20]
        country_code = line[2]
        num_departures = int(line[3])
        num_arrivals = int(line[4])
        expenditures = float(line[5])
        receipts = float(line[6])
        average_expenditures = 0
        average_receipts = 0
        if num_departures == 0:
            if num_arrivals != 0:
                average_expenditures = 0
                average_receipts = receipts/num_arrivals
                average_receipts = round(average_receipts, 2)
        elif num_arrivals == 0:
            if num_departures != 0:
                average_receipts = 0
                average_expenditures = expenditures/num_departures
                average_expenditures = round(average_expenditures, 2)
        elif num_arrivals == 0 and num_departures == 0:
            average_expenditures = 0
            average_receipts = 0
        else:
            average_expenditures = expenditures/num_departures
            average_expenditures = round(average_expenditures, 2)
            average_receipts = receipts/num_arrivals
            average_receipts = round(average_receipts, 2)
        num_arrivals = float(num_arrivals)
        num_departures = float(num_departures)
        receipts = float(receipts)
        expenditures = float(expenditures)
        tup = (year, country_name, country_code, num_arrivals/1000, \
                num_departures/1000, expenditures/1000000, receipts/1000000, \
                average_expenditures, average_receipts)
        if year == 2009:
            res[0].append(tup)
        elif year == 2010:
            res[1].append(tup)
        elif year == 2011:
            res[2].append(tup)
        elif year == 2012:
            res[3].append(tup)
        elif year == 2013:
            res[4].append(tup)
        elif year == 2014:
            res[5].append(tup)
        elif year == 2015:
            res[6].append(tup)
        elif year == 2016:
            res[7].append(tup)
        elif year == 2017:
            res[8].append(tup)
        
        for year in res:    
            year = sorted(year, key=itemgetter(1))    
            
    return res
        
def read_country_code_file(fp):
    '''
        read the country code file and return the sorted data
    '''
    country_list = []
    for line in fp:
        line = line.strip().split("/")
        country_list.append((line[0], line[1]))
    country_list.pop(0)
    res = sorted(country_list, key=itemgetter(0))
    
    return res      

def get_country_code_data(country_code, L):
    '''
        displays the country and the country code sorted as specified 
    '''
    res = []
    
    for year in L:
        for year_list in year:
            if year_list[2] == country_code:
                res.append(year_list)
    
    res = sorted(res, key = itemgetter(0))
    return res

def display_country_data(country_list):
    '''
       display the specified data for each country 
    '''
            
    # Get the country name from the list
    country_name = country_list[0][1]

    # Print table title
    title = "Travel Data for {}".format(country_name)
    print("\n{:^80s}".format(title))

    # headers
    header = ['Year', 'Departures','Arrivals','Expenditures', 'Receipts']
    units = ['','(thousands)','(thousands)','(millions)','(millions)']
    
    # header string formatting
    print('{:6s}{:>15s}{:>15s}{:>15s}{:>15s}'.format(header[0], header[1], header[2], header[3], header[4]))
    
    print('{:6s}{:>15s}{:>15s}{:>15s}{:>15s}'.format(units[0], units[1], units[2], units[3], units[4]))
    total_departures = 0
    total_arrivals = 0
    total_expenditures = 0
    total_receipts = 0
    for tup in country_list:
            print( "{:<6d}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}".format( tup[0], tup[4], tup[3], tup[5], tup[6] ))
            total_departures += tup[4]
            total_arrivals += tup[3]
            total_expenditures += tup[5]
            total_receipts += tup[6]
    print("")
    print("{:20s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}".format("Total", total_departures, total_arrivals, total_expenditures, total_receipts  ))
    
def display_year_data(year_list):
    '''
        display the yearly data for each country and the totals
    '''
    # Get the year from the list
    year = year_list[0][0]
    # Print table title
    
    title = "Travel Data for {:d}".format(year)
    print("\n{:^80s}".format(title))

    # Table headers
    header = ['Country Name', 'Departures','Arrivals','Expenditures',\
              'Receipts']
    units = ['','(thousands)','(thousands)','(millions)','(millions)']
    
    # header string formatting
    print("{:25s}{:15s}{:15s}{:15s}{:15s}".format(header[0], header[1], header[2], header[3], header[4]))
    
    # Rows string formatting
    print("{:25s}{:15s}{:15s}{:15s}{:15s}".format(units[0], units[1], units[2], units[3], units[4]))
    total_departures = 0
    total_arrivals = 0
    total_expenditures = 0
    total_receipts = 0
    for tup in year_list:
        if tup[0] == year:
            total_departures += tup[4]
            total_arrivals += tup[3]
            total_expenditures += tup[5]
            total_receipts += tup[6]
            print("{:20s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}".format(tup[1], tup[4], tup[3], tup[5], tup[6]))
    print("")
    print("{:20s}{:>15,.2f}{:>15,.2f}{:>15,.2f}{:>15,.2f}".format("Total", total_departures, total_arrivals, total_expenditures, total_receipts  ))
    print("")

def prepare_bar_plot(year_list):
    '''
        return two lists that will be used to plot a bar graph
    '''
    res1 = []
    res2 = []
    print(year_list)
    for item in year_list:
        country_name = item[1]
        average_expenditures = item[7]
        average_receipts = item[8]
        expenditure_tup = (country_name, average_expenditures)
        receipts_tup = (country_name, average_receipts)
        res1.append(expenditure_tup)
        res2.append(receipts_tup)
    res1 = sorted(res1, key = itemgetter(1), reverse = True)
    res1 = res1[:20]
    res2 = sorted(res2, key = itemgetter(1), reverse = True)
    res2 = res2[:20]
    return res1, res2

def prepare_line_plot(country_list):
    '''
        return two lists that will be used to plot a line graph
    '''
    res1 = []
    res2 = []
    
    for item in country_list:
        average_expenditures = item[7]
        average_receipts = item[8]
        res1.append(average_expenditures)
        res2.append(average_receipts)
           
    return res1, res2
    


def plot_bar_data(expend_list, receipt_list, year):
    '''
        This function plots the the top 20 countries with the highest average
        expenditures and the top 20 countries with the highest receipts.
        
        Returns: None
    
    '''
    pass
    # prepare the columns
    countries_expend = [elem[0] for elem in expend_list]
    values_expend = [elem[1] for elem in expend_list]
    
    countries_receipt = [elem[0] for elem in receipt_list]
    values_receipt = [elem[1] for elem in receipt_list]
    
    # Average expenditures
    
    x = range(20) # top 20 countries are to be plotted.

    fig, axs = plt.subplots(2, 1,figsize=(7,10))
    title = "Top 20 countries with highest average expenditures {:4d}".format(year)
    axs[0].set_title(title)
    axs[0].bar(x, values_expend, width=0.4, color='b')
    axs[0].set_ylabel("Avg. Expenditures (US dollar)")
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(countries_expend , rotation='90')
    
    # Average receipt
    title = "Top 20 countries with highest average receipt  {:4d}".format(year)
    axs[1].set_title(title)
    axs[1].set_ylabel("Avg. Receipts (US dollar)")
    axs[1].bar(x, values_receipt, width=0.4, color='b')
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(countries_receipt , rotation='90')
    fig.tight_layout()
    plt.show()
    
    ##comment the previous line and uncomment the following two lines when trying to pass Test 4
#    fig.savefig('avg_expense_receipts.png',dpi=100)
#    fig.clf()


def plot_line_data(country_code, expend_list, receipt_list):
    '''
        Plot the line plot for the expenditures and receipts for the
        country between 2009 and 2017
        
        Returns: None
    '''
    
    
    title = "Average expenditures and receipts for {} between 2009 and 2017".format(country_code)
    years = range(MIN_YEAR, MAX_YEAR+1)
    fig, axs = plt.subplots(figsize=(7,5))
    axs.set_title(title)
    axs.set_ylabel("Cost (US dollar)")
    axs.plot(years, expend_list, years, receipt_list)
    axs.legend(['Expenditures','Receipt'])

    plt.show()
    
    ##comment the previous line and uncomment the following two lines when trying to pass Test 4
#    fig.savefig('line.png',dpi=100)
#    fig.clf()

def main():
    '''
        loop through options for the user to select 
        call functions according to that function
        option 3 should display the country codes for reference 
        option 4 breaks out of the loop 
    '''
    
    BANNER = "International Travel Data Viewer\
    \n\nThis program reads and displays departures, arrivals, expenditures,"\
    " and receipts for international travels made between 2009 and 2017."
    
    # Prompt for option
    OPTION = "Menu\
    \n\t1: Display data by year\
    \n\t2: Display data by country\
    \n\t3: Display country codes\
    \n\t4: Stop the Program\
    \n\n\tEnter option number: "
    
    
    print(BANNER)
    print("")
    # YOUR CODE GOES HERE!
    travel_data = open_file("Enter the travel data file: ")
    country_code = open_file("Enter the country code file: ")
    print("")
    year_list = read_travel_file(travel_data)
    country_list = read_country_code_file(country_code)
    while True:
        inp = int(input(OPTION))
        if inp==1:
            year = int(input('Enter year: '))
            if year < 2009 or year > 2017:
                print('Year Not Valid')
                year = int(input('Enter Year: '))
            else:
                index = year - 2009
                year_list = year_list[index]
                display_year_data(year_list)

                plot = input('Do you want to plot (yes/no)? ').lower()
                if plot == 'yes':
                    prepare_bar_plot(year_list)
                else: 
                    continue
        elif inp==2:
            while True:
                country_code = input("Enter country code: ")
                country_code = country_code.upper()
                
                counter = 0
                for line in country_list:
                    if country_code == line[0]:
                        counter += 1
                        
                if counter > 0:
                    break
                else:
                    print("Country code is not found! Try Again!")
                    continue
                
            country_list = get_country_code_data(country_code, year_list)
            display_country_data(country_list)
            
            plot = input("Do you want to plot (yes/no)? ")
            if plot == 'yes':
                expend, receipt =  prepare_line_plot(display_country_data)
                plot_line_data(country_list,expend, receipt)
            else:
                continue
                



                    
        elif inp==3:
                print("Country Code Reference")
                print("Country Code   Country Name             ")
                for tup in country_list:
                    print(tup[0] + "            " + tup[1])
        elif (inp) == 4:
            print("Thanks for using this program!")
            break
        
if __name__ == "__main__":
    main()
    
