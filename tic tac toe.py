
tic_tac_toe = [
    
    [0,0,0],
    [0,0,0],
    [0,0,0],
    
    ]

print("use x and y for playing the game")
print("player 1 will use x")
print("player 2 will use y")
    
def print_func():    
    for i in tic_tac_toe:
        print(i)
        
def edit_board(rowloc,colloc,player):
    if player == 1:
        tic_tac_toe[rowloc][colloc] = "x"
    else:
        tic_tac_toe[rowloc][colloc] = "y"
        
def check_if_full(rowloc,colloc):
    if tic_tac_toe[rowloc][colloc] == 0:
        return False
    return True
def check_board_full():
    for i in tic_tac_toe:
        for j in i:
            if j == 0:
                return True
    return False
        
def take_input():
    rowloc = int(input("enter row location"))
    colloc = int(input("enter col location"))
    if rowloc<3 and colloc<3:
        return rowloc,colloc
    else:
        print("out of index")
        return take_input()
        
def check_if_win():
    win = False
    win_list3 = []
    win_list4 = []
    for i in range(len(tic_tac_toe)):
        win_list1 = []
        win_list2 = []
        for j in range(len(tic_tac_toe[i])):
            win_list1.append(tic_tac_toe[i][j])
            win_list2.append(tic_tac_toe[j][i])
        if 'x' in win_list1 and 'y' not in win_list1 and 0 not in win_list1:
            win = True
            return win , "Player 1 won"
        elif 'y' in win_list1 and 'x' not in win_list1 and 0 not in win_list1:
            win = True
            return win , "Player 2 won"
        elif 'x' in win_list2 and 'y' not in win_list2 and 0 not in win_list2:
            win = True
            return win , "Player 1 won"
        elif 'y' in win_list2 and 'x' not in win_list2 and 0 not in win_list2:
            win = True
            return win , "Player 2 won"
            
    for i in range(len(tic_tac_toe)):
        win_list3.append(tic_tac_toe[i][i])
    if 'x' in win_list3 and 'y' not in win_list3 and 0 not in win_list3:
        win = True
        return win , "Player 1 won"
    elif 'y' in win_list3 and 'x' not in win_list3 and 0 not in win_list3:
        win = True
        return win , "Player 2 won"
    del win_list3
    win_list4.append(tic_tac_toe[0][1])
    win_list4.append(tic_tac_toe[1][1])
    win_list4.append(tic_tac_toe[2][0])
    if 'x' in win_list4 and 'y' not in win_list4 and 0 not in win_list4:
        win = True
        return win , "Player 1 won"
    elif 'y' in win_list4 and 'x' not in win_list4 and 0 not in win_list4:
        win = True
        return win , "Player 2 won"
    del win_list4
    
    return win , ""
            

is_playable = True
count = 1
while is_playable:
    print_func()
    
    if not check_board_full():
        print("game is draw")
        break
    
    if count%2 !=0:
        print("it is player 1's turn")
        print("enter the location you want to enter your chance")
        rowloc,colloc = take_input()
        while check_if_full(rowloc,colloc):
            print("the location is full")
            rowloc,colloc = take_input()
        edit_board(rowloc,colloc,1)
    
        win,player_name = check_if_win()
        if win:
            print_func()
            print(player_name)
            break  
        
    else:
        print("it is player 2's turn")
        print("enter the location you want to enter your chance")
        rowloc = int(input("enter row location"))
        colloc = int(input("enter col location"))
        while check_if_full(rowloc,colloc):
            print("the location is full")
            rowloc = int(input("enter row location"))
            colloc = int(input("enter col location"))
        edit_board(rowloc,colloc,2)
    
        win,player_name = check_if_win()
        if win:
            print_func()
            print(player_name)
            break
    
    count+=1

