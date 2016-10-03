
def hasXWon():
    #diagonal
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0] is 'x':
        return 10
    if board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[2][0] is 'x':
        return 10
    #check row
    for i in range(0,3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0] is 'x':
            return 10

    #check column
    for i in range(0,3):
        if board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i] is 'x':
            return 10

    return 0

def hasoWon():

    #diagonal
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0] is 'o':
        return -10
    if board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[2][0] is 'o':
        return -10
    #check row
    for i in range(0,3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][0] is 'o':
            return -10

    #check column
    for i in range(0,3):
        if board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[0][i] is 'o':
            return -10

    return 0

def isBoardFull():

    for i in range(0,3):
         for j in range(0,3):
            if board[i][j]=='_':
                return False

    return True


def minimax(depth,isMax):
    scoreX=hasXWon()
    scoreo=hasoWon()
    
    if scoreX == 10:
        return scoreX
    
    if scoreo == -10:
        return scoreo

    if isBoardFull() is True:
        return 0

    if isMax is True:
        best=-1000

        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]=='_':
                    board[i][j]='x'
                    best=max(best,minimax(depth+1,False))
                    #print "_"*(depth+1)+str(best)+'--'+str(i)+','+str(j)
                    board[i][j]='_'
                    
        return best

    else:
        best=1000

        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]=='_':
                    board[i][j]='o'
                    best=min(best,minimax(depth+1,True))
                    #print "_"*(depth+1)+str(best)+'--'+str(i)+','+str(j)
                    board[i][j]='_'
        return best



def placeBestMove():

    if PcPlayer is 'x':

        bestVal=-1000
        bestMoveCoords=[-1,-1]

        for i in range(0,3):
            for j in range(0,3):

                if board[i][j]=='_':
                    board[i][j]='x'

                    moveVal=minimax(0,False)
                    #print 'X'+str(moveVal)+'--'+str(i)+','+str(j)
                    #print '' 
                    board[i][j]='_'

                    if moveVal>bestVal:
                        bestVal=moveVal
                        bestMoveCoords=[i,j]
                        
        placeOnBoard(bestMoveCoords[0],bestMoveCoords[1],PcPlayer)
        

    elif PcPlayer is 'o':
        
        bestVal=1000
        bestMoveCoords=[-1,-1]

        for i in range(0,3):
            for j in range(0,3):

                if board[i][j]=='_':
                    board[i][j]='o'                    
                    moveVal=minimax(0,True)
                    #print 'Y'+str(moveVal)+'--'+str(i)+','+str(j)   
                    #print ''
                    board[i][j]='_'
                    if moveVal<bestVal:
                        bestVal=moveVal
                        bestMoveCoords=[i,j]

        placeOnBoard(bestMoveCoords[0],bestMoveCoords[1],PcPlayer)



def userInput():
    x=input("Enter row")
    y=input("Enter column")
    x=int(x)
    y=int(y)
    placeOnBoard(x,y,player)

def placeOnBoard(x,y,ele):
    board[x][y]=ele
    printBoard()

def printBoard():
    for i in board:
        print i
    print ''


 
        

#-------------------------Main Logic----------------------------------


board=[
['_','_','_'],
['_','_','_'],
['_','_','_']
]

PcPlayer=''
player=''

choice=0
while choice!=1 or 2:
    choice=input("Who plays first \n1. Pc\n2. User ")

    if choice==1:
        PcPlayer='x'
        player='o'
        break
    elif choice==2:
        player='x'
        PcPlayer='o'
        break


if choice==1:
    placeBestMove()

else:
    userInput()


while isBoardFull()==False:


    if choice==1:
        userInput()
        if hasoWon() == -10:
            print 'O Won'
            break      
        
        placeBestMove()
          
        if hasXWon() == 10:
            print 'X Won'
            break
        

    else:
    
        placeBestMove()
        
        if hasoWon() == -10:
            print 'O Won'
            break
        
        userInput()

        if hasXWon() == 10:
            print 'X Won'
            break
    
if hasXWon()==0 and hasoWon()==0 and isBoardFull()==True:
    print "DRAW"
