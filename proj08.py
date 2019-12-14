"""
    computer project #8
    scrabble game 
    use try except to open a file 
    read the file and return a dictionary of viable words 
    calculate the score of each word and return a set 
    generate combinations of usable words 
    generate words that are in the english dictionary 
    calculate the score for those words
    sort the words by score and length 
    display the words in a specified format 
    call main to display the words that match the rack and the placed tile that the user inputs  
"""
SCORE_DICT = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

import itertools
from operator import itemgetter

def open_file():
    '''
        use try except to open a file 
    '''
    while True:
        #Iterating until correct path is fount
        filename = input("Input word file: ")
        try:
            #Escaping if wrong path
            fp = open(filename, "r")
            break
        except FileNotFoundError:
            continue
    return fp


def read_file(fp):
    """
    read the file line by line and return a dictionary of words 
    """
    scrabble_words_dict = {}
    
    for line in fp:
        line = line.lower()
        line = line.strip()
        if len(line) < 3:
            continue
        elif "-" in line or "'" in line:
            continue
        else:
            scrabble_words_dict[line] = 1
    return scrabble_words_dict

def calculate_score(rack,word):
    """
    calculate the socre of the word that is used 
    """
    score = 0

    for letter in word:
        score += SCORE_DICT[letter]
    if len(rack) < 7:
        score = score
    else:
        if len(word) >= len(rack):
            score = (score + 50)
    return score

def generate_combinations(rack,placed_tile):
    """
    generate all combinations that the user can input into the game return a set of those words
    """
    combinations_set = set()
    if placed_tile == "":
        for i in range(3, (len(rack)+1)):
            for x in itertools.combinations(rack, i):
                combinations_set.add(x)
    else:
        word = rack+placed_tile
        for i in range(3, (len(word)+1)):
            for x in itertools.combinations(word, i):
                if placed_tile in x:
                    combinations_set.add(x)
          
    return combinations_set

def generate_words(combo,scrabble_words_dict):    
    """
    generate english words based on the combinations , return a word set 
    """
    word_set = set()
    for w in itertools.permutations(combo):
        word = ''.join(w)
        if word in scrabble_words_dict:
            word_set.add(word)
    return word_set

def generate_words_with_scores(rack,placed_tile,scrabble_words_dict):
    """
    generate the word and corresponding score, return a dictionary where the key is the word and the 
    value is the score 
    """
    res_set = set()
    word_score_dict = {}
    comb_set = generate_combinations(rack,placed_tile)
    for combo in comb_set:
        words_set = generate_words(combo, scrabble_words_dict)
        for word in words_set:
            res_set.add(word)
    for word in res_set:
        score = calculate_score(rack,word)
        word_score_dict[word] = score
    return word_score_dict
    

def sort_words(word_dic):
    """
    sort the words based on score then based on length in descending order 
    """
    word_list = []
    for key, value in word_dic.items():
        word = key
        score = value
        tup = (word, score, len(word))
        word_list.append(tup)
    word_list = sorted(word_list, key=itemgetter(0))
    length_list = sorted(word_list, key=itemgetter(2, 1), reverse = True)
    score_list = sorted(word_list, key=itemgetter(1, 2), reverse = True)
    return score_list, length_list
        

def display_words(word_list,specifier):
    """
    display the top 5 words in the specified manner 
    """
    
    if specifier.lower() == 'score':
        print("{:>6s}  -  {:s}".format("Score", "Word"))
        if len(word_list) < 5:
            for tup in word_list:
                print("{:>6d}  -  {:s}".format(tup[1], tup[0]))
        else:
            
            for tup in word_list[:5]:
                print("{:>6d}  -  {:s}".format(tup[1], tup[0]))
                
                
    elif specifier.lower() == 'length':
        print("{:>6s}  -  {:s}".format("Length", "Word"))
        if len(word_list) < 5:
            for tup in word_list:
                print("{:>6d}  -  {:s}".format(tup[2],  tup[0]))
        else:
            
            for tup in word_list[:5]:
                print("{:>6d}  -  {:s}".format(tup[2], tup[0]))      
            

def main():
    """
    display the words based on the user input of rack and placed tiles
    """
    print("Scrabble Tool")
    user_inp = input("Would you like to enter an example (y/n): ").lower()

    while user_inp:
        
        if user_inp == 'y':
            fp = open_file()
            scrabble_words_dict = read_file(fp)
            rack = input("Input the rack (2-7chars): ")
            while rack:
                if len(rack) < 2 or rack.isalpha() == False:
                    rack = input("Input the rack (2-7chars): ")
                elif len(rack) > 7 or rack.isalpha() == False:
                    rack = input("Input the rack (2-7chars): ")
                else:
                    break
            placed_tiles = input("Input tiles on board (enter for none): ")
            while placed_tiles:
                if placed_tiles.isalpha() == False:
                    if placed_tiles ==  "":
                        break
                    else:
                        placed_tiles = input("Input tiles on board (enter for none): ")
                else:
                    break
            res_dic = {}
            if placed_tiles == "":
                res_dic.update(generate_words_with_scores(rack,"",scrabble_words_dict))
            else:
                for ch in placed_tiles:
                    res_dic.update(generate_words_with_scores(rack,ch,scrabble_words_dict))
                
            score_list, length_list = sort_words(res_dic)
            print("Word choices sorted by Score")
            display_words(score_list, "score")
            print(" ")
            print("Word choices sorted by Length")
            display_words(length_list, "length")
            user_inp = input("Do you want to enter another example (y/n): ").lower()
        else:
            print("Thank you for playing the game")
            break
    

                    
            
            

if __name__ == "__main__":
    main()