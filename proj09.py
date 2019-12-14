"""
    computer project 09 
    breach data 
    open file
    iterate through file 
    build dictionary 
    sort the top records by entity 
    sort the top records by year 
    create a main function to ask the user and display the data accordingly 
"""

import csv
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

def open_file(message):
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    
    while True:
        #Iterating until correct path is fount
        filename = input(message)
        try:
            #Escaping if wrong path
            fp = open(filename, "r", encoding = "utf8")
            break
        except FileNotFoundError:
            if message == '':
                fp = open("breachdata.csv", "r", encoding= "utf8" )
                break
            else:
                print('File not found! Try Again!')
                continue
    return fp
    
    
def build_dict(reader):
    
    next(reader, None)
    master_dict = {}
    for line in reader:
        if (line[11] and line[0] and line[3] and line[4] and line[5] and line[6] ):
            if not line[2].strip():
                lost_records = 0
            else:
                try:
                    lost_records = int(line[2].strip().replace(',',''))
                except ValueError:
                    lost_records = 0
            try:
                year = int(line[3])
            except ValueError:
                continue
            story = line[4].strip()
            entity = line[0].strip()
            news_sources = line[11].split(',')
            sector = line[5].strip()
            method = line[6].strip()
        d1 = {entity:(lost_records, year, story, news_sources)}
        d2 = {year: (sector, method)}
        tup = (d1,d2)
        if entity in master_dict:
            master_dict[entity].append(tup)
        else:
            master_dict[entity] = [tup]
    return master_dict

        
def top_rec_lost_by_entity(dictionary):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    top_recs_lost = []

    for key, value in dictionary.items():
        records_lost = 0
        entity = key
        for tup in value:
            for dic in tup:
                for key, value in dic.items():
                    try:
                        int(key)
                        continue
                    except ValueError:
                        if entity == key:
                            records_lost += value[0]
                        else:
                            records_lost = value[0]
        tup = (entity, records_lost)
        top_recs_lost.append(tup)
        top_recs_lost = sorted(top_recs_lost, key=itemgetter(1), reverse = True)
    return top_recs_lost[:10]

def records_lost_by_year(dictionary):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    res = []
    year_dic = {}
    for key, value in dictionary.items():
        for tup in value:
            for dic in tup:
                for key, value in dic.items():
                    try:
                        int(key)
                        continue
                    except ValueError:
                        year = value[1]
                        if year in year_dic:
                            year_dic[year] += value[0]
                        else:
                            year_dic[year] = value[0]
                    
    for key, value in year_dic.items():
        year = key 
        records_lost = value
        tup = (year, records_lost)
        res.append(tup)
            
    res.sort(key=itemgetter(1), reverse = True)
    return res  
    

def top_methods_by_sector(dictionary):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    sector_dic = {}
    for key, value in dictionary.items():
        for tup in value:
            for dic in tup:
                for key, value in dic.items():
                    try:
                        int(key)
                        sector = value[0]
                        method = value[1]
                        if sector in sector_dic:
                            sector_dic[sector] = dict()
                            if method in sector_dic[sector]:
                                sector_dic[sector][method] += 1
                            else:
                                sector_dic[sector][method] = 1
                        else:
                            sector_dic[sector] = dict()
                            sector_dic[sector][method] = 1
                    except ValueError:
                       continue
    return sector_dic
        
def top_rec_lost_plot(names,records):
    ''' Plots a bargraph pertaining to
        the cybersecurity breaches data '''
        
    y_pos = np.arange(len(names))

    plt.bar(y_pos, records, align='center', alpha=0.5,
            color='blue',edgecolor='black')
    plt.xticks(y_pos, names, rotation=90)
    plt.ylabel('#Records lost')
    plt.title('Cybersecurity Breaches',fontsize=20)
    plt.show()
    
def top_methods_by_sector_plot(methods_list):
    ''' Plots the top methods used to compromise
        the security of a sector '''
    methods = [] ; quantities = []
    for tup in methods_list:
        methods.append(tup[0])
        quantities.append(tup[1])
    labels = methods
    sizes = quantities
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    plt.pie(sizes, labels=labels, colors = colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    
    plt.axis('equal')
    plt.show()
    
def main():
    BANNER = '''
    
                 _,.-------.,_
             ,;~'             '~;, 
           ,;                     ;,
          ;                         ;
         ,'                         ',
        ,;                           ;,
        ; ;      .           .      ; ;
        | ;   ______       ______   ; | 
        |  `/~"     ~" . "~     "~\'  |
        |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
         |   |        }:{        |   | 
         |   l       / | \       !   |
         .~  (__,.--" .^. "--.,__)  ~. 
         |     ---;' / | \ `;---     |  
          \__.       \/^\/       .__/  
           V| \                 / |V  
            | |T~\___!___!___/~T| |  
            | |`IIII_I_I_I_IIII'| |  
            |  \,III I I I III,/  |  
             \   `~~~~~~~~~~'    /
               \   .       .   /
                 \.    ^    ./   
                   ^~~~^~~~^ 
                   
           
           ~~Cybersecurity Breaches~~        
                   @amirootyet    
                
    '''
    
    print(BANNER)
    
    MENU = '''  
[ 1 ] Most records lost by entities
[ 2 ] Records lost by year
[ 3 ] Top methods per sector
[ 4 ] Search stories
[ 5 ] Exit

[ ? ] Choice: '''
    
    choice = input(MENU)
    while choice:
        if choice == '1' or choice == '2' or choice == '3' or choice == '4':
            message = input('[ ? ] Enter the file name: ')
            fp = open_file(message)
            reader = csv.reader(fp)
            breach_dic = build_dict(reader)
            if choice == '1':
                print('[ + ] Most records lost by entities...')
                entity_records = top_rec_lost_by_entity(breach_dic)
                
                value = 0
                for tup in entity_records:
                    value += 1
                    print('---------------------------------------------')
                    print("[ {:2d} ] | {:15.10s} | {:10d}".format( (value), tup[0], tup[1] ))
                    
                plot_inp = input('[ ? ] Plot (y/n)? ')
                if plot_inp == 'y':
                    names = []
                    records = []
                    for tup in entity_records:
                        names.append(tup[0])
                        records.append(tup[1])
                    top_rec_lost_plot(names, records)
                else:
                    print(MENU)
                    print('[ + ] Done. Exiting now...')
                    break
            if choice == '2':
                print('[ + ] Most records lost in a year...')
                year_records = records_lost_by_year(breach_dic)
                value = 0 
                for item in year_records:
                    value += 1
                    print('---------------------------------------------')
                    print("[ {:2d} ] | {:<15d} | {:10d}".format(value, item[0], item[1]))
                plot_inp = input('[ ? ] Plot (y/n)? ')
                if plot_inp == 'y':
                    years = []
                    records = []
                    for tup in year_records:
                        years.append(tup[0])
                        records.append(tup[1])
                    top_rec_lost_plot(years, records)
                else:
                    print(MENU)
                    print('[ + ] Done. Exiting now...')
                    break
            if choice == '4':
                entity_inp = input('[ ? ] Name of the entity (case sensitive)? ')
                res = []
                while entity_inp not in breach_dic:
                    print("[ - ] Entity not found. Try again.")
                    entity_inp = input('[ ? ] Name of the entity (case sensitive)? ')
                print("[ - ] Entity not found. Try again.")
                print('[ ? ] Name of the entity (case sensitive)? ')
                stories = breach_dic[entity_inp]
                print("[ + ] Found {} stories:".format(len(stories)))
                for i in stories:
                    other_story = i[0].values()
                    for x in other_story:
                        res.append(x[2])
                count = 0
                for i in range(len(res)):
                    count += 1
                    print("[ + ] Story {}: {:10s}".format(count, res[i]))
                choice = input(MENU)
        elif choice == '5':
            print('[ + ] Done. Exiting now...')
            break
        else:
            print("[ - ] Incorrect input. Try again.")
            choice = input(MENU)
            

if __name__ == "__main__":
     main()
     
     
