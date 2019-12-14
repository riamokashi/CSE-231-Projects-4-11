########################################
# Computer Project 06
#
# file iteration with lists and tuples 
# create functions --open a file -- read a file -- remove duplicate websites -- display top sites per country -- display top sites per page view -- prompt user -- key word search 
#
# open file 
    # open specified file by user 
# read file 
    #create a list of tuples of information in the file 
# duplicates
    # remove the same website domains from the websities list 
# top sites 
    # display top 20 sites per counrty in specified order 
# top sites 2
    # display top 20 sites per page views in decending order 
#main function 
    # prompt user to select an option and call the specified function to do the job 
# key work search 
    # user enters a key word and is able to find all domains containing that word 
########################################

import csv
from operator import itemgetter

PROMPT = '''
Choose
         (1) Top sites by country
         (2) Search by web site name
         (3) Top sites by views
         (q) Quit      
'''

print("----- Web Data -----")
def open_file():
    '''Docstring goes here.'''
    
    file_input = input("Input a filename: ") # user inputs a file name 
    try:
        fp = open(file_input, "r", encoding="ISO-8859-1") # try exept in order to check if the file can be opened, encoding is for .csv files specifically 
        return fp
    except FileNotFoundError: # error message displayed if the .csv file fails to be found 
        print("Error: file not found.") # print error message and repromt the user 
        open_file() # call open file again to test the new input for the file name 


def read_file(fp):
    '''returns a tuple with country rank, website, traffic rank, average daily views, and country name'''

    reader = csv.reader(fp) # create a reader for the file 
    next(reader, None) # skip the header of the file 
    L_of_L = [] # concatenate an empty list that will be filled with the correct information (the specified tuple)
    for line in reader: # iterate through each line in the file
        # grab each index for the specified information 
        country_rank = line[0].strip() #. strip to remove all white space before and after 
        website = line[1].strip()
        traffic_rank = line[14].strip().replace(" ", "") #.replace to get rid of all white space 
        avg_daily_pageviews = line[5].strip().replace(" ", "")
        country = line[30].strip()
        # use try exept to make the strs into ints 
        try:
            country_rank = int(country_rank)
            traffic_rank = int(traffic_rank)
            avg_daily_pageviews = int(avg_daily_pageviews)

            info = (country_rank,website,traffic_rank,avg_daily_pageviews,country) # if it is an integer, then fill up the empty list with the specified information 

            L_of_L.append(info) # add that info into the concatenated list 
        except:
            continue # if not just skip the line 

    L_of_L = sorted(L_of_L,key=itemgetter(0,4)) # sort the infomation in the specified order 

    return L_of_L # return the sorted list that will be used in following functions 

def remove_duplicate_sites(L_of_L):
    '''Remove duplicate sites'''
    res = [] # concatenate an empty list for the resulting L_of_L
    domains = [] # concatenate an empty list for the website domains after the cuts have been made

    for tup in L_of_L: # grab the website index
        first_index = tup[1].find(".") # find the index of the right justified "."
        end = tup[1][first_index + 1:].find(".") + 4
        domain = tup[1][:end] # cut the end off after that index
        

        if domain not in domains: # if the website is not in the domains
            domains.append(domain) # add the website to the non duplicates list
            res.append(tup) # add the tuple to the resulting L_of_L

    res = sorted(res,key=itemgetter(0,1)) # sort the resulting list of tuples by specified instructions

    return res # return the sorted list of tuples


def top_sites_per_country(L_of_L,country):
    '''display the top sites per country'''

    res = [] # concatenate an empty list for the top sites to be appeneded to 

    for tup in L_of_L: # grab the country index
        if tup[4] == country: # if the country exists 
            res.append(tup) # add it to the tuple 

    res = sorted(res,key=itemgetter(0)) # sort by the country rank 
    res = res[:20] # cut it off at index 20 becuase only the top 20 are wanted 

    return res # return the sorted and cut list

def top_sites_per_views(L_of_L):
    '''Rank the top sites per page views in decending order'''
    L_of_L = remove_duplicate_sites(L_of_L)
    L_of_L = sorted(L_of_L, key=itemgetter(3,0), reverse = True)
    L_of_L = L_of_L[:20]
    

    return L_of_L

def main():
    '''Enable the user to pick which option they want to select and execute that option(function)'''

    fp = open_file() # create a variable to store the file 
    L_of_L = read_file(fp) # read the file and store it in the list variable 

    exit = False #create a false statement so a 'break' is not required in the loop 
    
    while(not exit): # while true 
        print(PROMPT) # print the prompt so the user can see the options to select from 
        
        option_input = input("Choice: ").lower() # allow user to input an option and make it lowercase so the the str 'q' and 'Q' is recognized as the same input 

        if option_input == '1': # if the first option is selected 
            print("--------- Top 20 by Country -----------")
            country = input("Country: ").split() # capitalize the country so that the function can take it in as a string (since all country names are capitalized in the file )
            string = " "
            for word in country:
                string += word.capitalize() + " " 
            country = string.strip()
            l1 = L_of_L.copy()
            res = top_sites_per_country(l1,country)
            print(" {:30s} {:>15s}{:>30s}".format("Website", "Traffic Rank", "Average Daily Page Views"))
            for item in res:  
                print(" {:30s} {:>15d}{:>30,d}".format(item[1], item[2], item[3]))
                
        elif option_input == '2': # if the second option is selected 
            keyword = input("Search: ").lower() #input the key word to search through the domains with and makes it lower case

            res = [] # concatenate an empty list so that it can be filled with all the domains containing that key word that the user inputed

            for tup in L_of_L: # interate through the tuples 
                if keyword in tup[1]: # grab the website index if the keyword is in the tuple 
                    res.append(tup[1]) # the add that domain to the concatenated list 

            print("{:^50s}".format("Websites Matching Query")) # format in the desired formatting specifications 

            if len(res) == 0: # if no domains exist with that key word 
                print("None found") # print that it is not found 
            else:
                for website in res: #or else for each website in the list 
                    print(website) # print the website name 


        elif option_input == '3': # if the third option is selected 
            print("--------- Top 20 by Page View -----------")
            l2 = L_of_L.copy()
            res = top_sites_per_views(l2) # store the list from the function in the variable 
            print("{:30s} {:>15s}".format("Website", "Ave Daily Page Views"))
            #print res based on professor guidelines
            for item in res:
                print("{:30s} {:>20,d}".format(item[1], item[3]))
                
        elif option_input == 'q': # if the user wants to quit
            exit = True # make the loop false to end the loop completely 
        else:
            print("Incorrect input. Try again.")

if __name__ == "__main__":
     main()