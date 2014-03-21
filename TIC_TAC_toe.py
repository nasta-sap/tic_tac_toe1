def print_box(box):
# This function prints the playing field   
    print "Box:"
    for row in box:
        print " ".join(row)
def your_move (box,side):
# Ход игрока    
    flag=True
    while flag:
        row=int(raw_input("Guess Row: "))
        col=int(raw_input("Guess Col: "))
        if row<0 or col<0 or row>=3 or col>=3:
            print "The value should be in range [0;2]. Enter the coordinates again."
        elif box[row][col]=='-':
            box[row][col]=side
            flag=False
        else:        
            print "This square is occupied. Enter the coordinates again."
	    
    return box
def your_side(side):
# Select x or o (for the first player)  
    k=0
    while side!='o' and side!='x':
        if k==1:
            print "Be careful! You should enter 'x' or 'o'"
        side=raw_input("Choose your side (x or o):")
        k=1
    return side    
def comp_move(box,side1):
# The computer's move (when you select a single player game)    
    flag=True
    while flag:
        row=randint(0, len(box) - 1)
        col=randint(0, len(box) - 1)
        if box[row][col]=='-':
            box[row][col]=side1
            flag=False     
    return box            
            
def win(box,side):
# This function checks, won if a player side. Yes: True, not False   
    for i in range (2):
        if box[i][0]==box[i][1]==box[i][2]==side or box[0][i]==box[1][i]==box[2][i]==side or box[0][0]==box[1][1]==box[2][2]==side or side==box[0][2]==box[1][1]==box[2][0]:
            print side,' win!'
            return True
        else:
            return False
def number_players ():
# A request to the number of players. 1: 2 False: True
    number=int(raw_input("Enter the number of players (1 or 2)."))
    if number==2:
        return True
    else:
        return False
# Main
from random import randint        
box = []
print 
for x in range(0,3):
    box.append(["-"] * 3)
print "Hello"
print "Let's play TIC-TAC-toe!"
print "Firstly:"
second_player=number_players()
side='-'
side=your_side(side)
if side=='o':
    side1='x'
else:
    side1='o'
print_box(box)
flag=True
count=0
while count<8:
    box=your_move(box,side)
    count+=1
    print_box(box)
    if win(box,side):
        break;
    if second_player:
        box=your_move(box,side1)
    else:    
        box=comp_move(box,side1)
    count+=1
    print_box(box)
    if win(box,side1):
        break
else:
    print "Drawn game!"
