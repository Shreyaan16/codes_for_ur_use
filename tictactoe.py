grid_dict={'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def display_matrix():
     print("The grid looks like: ")
     print(f"{grid_dict['1']} | {grid_dict['2']} | {grid_dict['3']} \n--|---|--\n{grid_dict['4']} | {grid_dict['5']} | {grid_dict['6']} \n--|---|--\n{grid_dict['7']} | {grid_dict['8']} | {grid_dict['9']}")


def want_to_play():
        grid_dict={'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        def display_matrix():
            print("The grid looks like: ")
            print(f"{grid_dict['1']} | {grid_dict['2']} | {grid_dict['3']} \n--|---|--\n{grid_dict['4']} | {grid_dict['5']} | {grid_dict['6']} \n--|---|--\n{grid_dict['7']} | {grid_dict['8']} | {grid_dict['9']}")
        flag=True
        choice=input("Do you want to play the game? press y for yes or n for no: ")
        if choice=='y' or choice=='Y':
            print("Welcome to the Game :)")
            print("This is a general tic-tac-toe game but in this you can take any symbol you want")
            symbol1=input("Enter the symbol for player one: ")
            symbol2=input("Enter the symbol for symbol two: ")
            def check_draw():
                return all(symbol in [symbol1,symbol2] for symbol in grid_dict.values())
            display_matrix()
            while flag==True:
                print("Player-1's turn:")
                loc1=input("Enter the location number you want to change from the grid: ")
                while loc1.isdigit()==False:
                    print("Enter one of the locations on the grid")
                    loc1=input("Enter the location number you want to change from the grid: ")
                while int(loc1) not in [1,2,3,4,5,6,7,8,9]:
                    print("Enter valid number")
                    loc1=input("Enter the location number you want to change from the grid: ")
                else:
                    grid_dict[loc1]=symbol1
                    display_matrix()
                if grid_dict['1']==grid_dict['2']==grid_dict['3'] or grid_dict['1']==grid_dict['4']==grid_dict['7'] or grid_dict['4']==grid_dict['5']==grid_dict['6'] or grid_dict['7']==grid_dict['8']==grid_dict['9'] or grid_dict['2']==grid_dict['5']==grid_dict['8'] or grid_dict['3']==grid_dict['6']==grid_dict['9'] or grid_dict['1']==grid_dict['5']==grid_dict['9'] or grid_dict['3']==grid_dict['5']==grid_dict['7']:
                    flag=False
                    print("Player 1 won the game:")
                    want_to_play()
                    break
                elif check_draw():
                    print("Game is draw")
                    want_to_play()
                    break
                print("Player-2's turn:")
                loc2=input("Enter the location number you want to change from the grid: ")
                while loc2.isdigit()==False:
                    print("Enter one of the locations on the grid")
                    loc2=input("Enter the location number you want to change from the grid: ")
                while int(loc2) not in [1,2,3,4,5,6,7,8,9]:
                    print("Enter a valid ")
                    loc2=input("Enter the location number you want to change from the grid: ")
                else:
                    grid_dict[loc2]=symbol2
                    display_matrix()
                if grid_dict['1']==grid_dict['2']==grid_dict['3'] or grid_dict['1']==grid_dict['4']==grid_dict['7'] or grid_dict['4']==grid_dict['5']==grid_dict['6'] or grid_dict['7']==grid_dict['8']==grid_dict['9'] or grid_dict['2']==grid_dict['5']==grid_dict['8'] or grid_dict['3']==grid_dict['6']==grid_dict['9'] or grid_dict['1']==grid_dict['5']==grid_dict['9'] or grid_dict['3']==grid_dict['5']==grid_dict['7']:
                    flag=False
                    print("Player-2 won the game")
                    want_to_play()
                    break
                elif check_draw():
                    print("Game is draw")
                    want_to_play()
                    break
        elif choice=='n' or choice=='N':
            print("Thanks for playing")
        else:
            print("Please input a valid choice if u want to play")
            want_to_play()

want_to_play()

print("End of game")


