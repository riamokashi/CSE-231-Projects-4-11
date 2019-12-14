"""
    computer proj 10 
    card game 
    create functions to test the validity of moves 
    execute moves
    initialize the game by creating a stock, tableau and foundation
    deal cards to the tableau 
    display the cards appropriately 
    get the option
    validate the move from the tableau to the foundation 
    move card to foundation if valid 
    validate the move within the tableau 
    move card within the tableau if valid 
    check to see if the user has won 
    create a main function that prompts user to inputs and executes the choice correctly so the game can be played
"""


import cards  # required !!!

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
        of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    tableau = [[], [], [], []]
    foundation = []
    stock = cards.Deck()
    stock.shuffle()
    for tup in tableau:
        tup.append(stock.deal())
    
    return (stock, tableau, foundation)  # stub so that the skeleton compiles; delete 
                               # and replace it with your code
    
def deal_to_tableau( stock, tableau ):
        
    '''
        WRITE DOCSTRING HERE!!!
    '''
 
    for tup in tableau:
        tup.append(stock.deal())


def display( stock, tableau, foundation ):
    '''Display the stock, tableau, and foundation.'''
    
    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    
    # determine the number of rows to be printed -- determined by the most
    #           cards in any tableau column
    max_rows = 0
    for col in tableau:
        if len(col) > max_rows:
            max_rows = len(col)

    for i in range(max_rows):
        # display stock (only in first row)
        if i == 0:
            display_char = "" if stock.is_empty() else "XX"
            print("{:<8s}".format(display_char),end='')
        else:
            print("{:<8s}".format(""),end='')

        # display tableau
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print("{:4s}".format( str(col[i]) ), end='' )

        # display foundation (only in first row)
        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')

        print()

def get_option():
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    option = []
    print(RULES)
    choice = input(MENU)
    if choice == 'D':
        option.append(choice)
    elif 'F' in choice:
        choice.split()
        for item in choice:
            option.append(item)
    elif 'T' in choice:
        choice.split()
        for item in choice:
            option.append(item)
    elif choice == 'R':
        option.append(choice)
    elif choice == 'H':
        option.append(choice)
    elif choice == 'Q':
        option.append(choice)
    
    return option   # stub; delete and replace with your code
            
def validate_move_to_foundation( tableau, from_col ):
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    from_col = int(from_col)

    if  (1 <= from_col <= 4):
        if len(tableau[(from_col)-1]) != 0:
            card = tableau[(from_col)-1][-1]
            if card.rank() == 1:
                if card.suit() == 4:
                    print('Error, cannot move A♠.')
                elif card.suit() == 1:
                    print('Error, cannot move A♣.')
                elif card.suit() == 2:
                    print('Error, cannot move A♦.')
                elif card.suit() == 3:
                    print('Error, cannot move A♥.')
                return False
            for tup in tableau:
                for line in tup:
                    if len(tup) != 0:
                        line = tup[-1]
                        if line.suit() == card.suit():
                            if line.rank() == 1:
                                return True
                            elif line.rank() > card.rank():
                                return True
                    else:
                        continue
            else:
                if card.rank() == 13:
                    if card.suit() == 4:
                        print('Error, cannot move K♠.')
                    elif card.suit() == 1:
                        print('Error, cannot move K♣.')
                    elif card.suit() == 2:
                        print('Error, cannot move K♦.')
                    elif card.suit() == 3:
                        print('Error, cannot move K♥.')
                else:
                    if card.suit() == 4:
                        print('Error, cannot move ' + str(card.rank()) + '♠.')
                    elif card.suit() == 1:
                        print('Error, cannot move ' + str(card.rank()) +  '♣.')
                    elif card.suit() == 2:
                        print('Error, cannot move ' + str(card.rank()) +  '♦.')
                    elif card.suit() == 3:
                        print('Error, cannot move ' + str(card.rank()) +  '♥.')
                    
                return False
        else:
            print('Invalid move')
            return False
    else:
        print('Invalid move')
        return False
        

    
def move_to_foundation( tableau, foundation, from_col ):
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    # call validate function 
    valid_bool = validate_move_to_foundation( tableau, from_col )
    
    if valid_bool:
        #move a card from tableau to foundation
        card = tableau[(from_col)-1][-1]
        foundation.append(card)
        for column in tableau:
            if card in column:
                column.pop()
                
        

def validate_move_within_tableau( tableau, from_col, to_col ):
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    if (1 <= from_col <= 4 and 1 <= to_col <= 4):
        if len(tableau[(from_col)-1]) == 0:
            print('Invalid move')
            return False
        elif len(tableau[(to_col)-1]) == 0:
            return True
        else:
            print('Invalid move')
            return False
    else:    
        print('Invalid move')
        return False  



def move_within_tableau( tableau, from_col, to_col ):
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    valid_bool = validate_move_within_tableau( tableau, from_col, to_col )
    if valid_bool:
        card = tableau[(from_col)-1][-1]
        for column in tableau:
            if card in column:
                tableau[(to_col)-1] = [card]
                column.pop()
                

        
def check_for_win( stock, tableau ):
    
    '''
        WRITE DOCSTRING HERE!!!
    '''
    for tup in tableau:
        if len(tup) < 2:
            for card in tup:
                if card.value() == 1 and len(stock) == 0:
                    status = True
                    continue
                else:
                    return False
                    break
        else:
            return False
            break
    return status
        
def main():
        
    '''
        WRITE DOCSTRING HERE!!!
    '''
 
    stock, tableau, foundation = init_game()
    print( MENU )
    display( stock, tableau, foundation )
    
    while True:
        option = input('\nInput an option (DFTRHQ): ')
        option1 = option.strip()
        # Your code goes here
        if option1.lower() == 'h':
            print(MENU)
        elif option1.lower() == 'd':
            deal_to_tableau( stock, tableau )
        elif option1.lower() == 'r':
            print('=========== Restarting: new game ============')
            print(RULES)
            print(MENU)
            (stock, tableau, foundation) = init_game()
        elif option1.lower() == 'q':
            print('You have chosen to quit.')
            break
        elif 'f' in option1.lower():
            choice = option1.strip()
            choice = choice.split()
            if choice[1].isalpha() == True:
                print('Error in option: ' + option)
                print('Invalid option.')
                
            else:    
                for item in choice:
                    try:
                        int(item)
                        move_to_foundation( tableau, foundation, int(item))
                    except ValueError:
                        continue
                if check_for_win( stock, tableau ) == True:
                    print('You won!')
                    break
            
        elif 't' in option1.lower():
            choice = option1.strip()
            choice = choice.split()
            if len(choice) == 2:
                print('Error in option: ' + option)
                print('Invalid option.')                
            elif choice[1].isalpha == True or choice[2].isalpha() == True:
                print('Error in option: ' + option)
                print('Invalid option.')
            else:    
                move_within_tableau( tableau, int(choice[1]), int(choice[2]) )
                if check_for_win( stock, tableau ) == True:
                    print('You won!')
                    break
        else:
            print('Error in option: ' + option)
            print('Invalid option.')
            
        display( stock, tableau, foundation)

if __name__ == "__main__":
    main()